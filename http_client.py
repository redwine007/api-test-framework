# 封装 HTTP 请求细节。
# 业务判断不要和 requests 细节耦合，后面好替换/好测试。
import time

import requests

import uuid
from typing import Optional


def _new_request_id() -> str:
    """
    生成一次请求的唯一 ID
    """
    return str(uuid.uuid4())


def build_default_headers() -> dict[str, str]:
    """
    默认 headers：
    - X-Request-Id：一次 HTTP 调用一个 ID、
    """
    return {
        "X-Request-Id": _new_request_id(),
        "Accept": "application/json",
    }


def build_auth_headers(token: str) -> dict[str, str]:
    """
    Bearer 鉴权：
    - token 为空：不加 Authorization（避免无效头干扰）
    """
    token = token.strip()
    if not token:
        return {}

    return {"Authorization": f"Bearer {token}"}


def create_session(token: str) -> requests.Session:
    """
    - requests.Session 复用底层 TCP 连接（连接池）
    - 把默认 headers 设置在 session 上，后续每次请求自动带
    """
    session = requests.Session()

    merged = {**build_default_headers(), **build_auth_headers(token)}
    session.headers.update(merged)
    return session


def http_get(
    url: str,
    timeout: int,
    token: str = "",
    retries: int = 2,
    retry_interval: float = 0.5,
    session: Optional[requests.Session] = None,
) -> requests.Response:
    """
    发送 GET 请求并返回 Response 对象。

    参数：
    - url: 请求地址
    - timeout: 超时时间（秒）
    - retries: 失败后最多重试次数（不含第一次）
    - retry_interval: 每次重试前等待秒数
    返回：
    - requests.Response：包含 status_code、headers、text/json 等
    """
    owns_session = False
    if session is None:
        session = create_session(token)
        owns_session = True
    last_error: Optional[Exception] = None
    try:
        for attempt in range(retries + 1):
            try:
                per_request_headers = {"X-Request-Id": _new_request_id()}
                return session.get(url, timeout=timeout, headers=per_request_headers)
            except requests.RequestException as e:
                last_error = e
                if attempt < retries:
                    time.sleep(retry_interval)
                else:
                    raise last_error
    finally:
        # Session 需要关闭（释放连接池资源）
        # owns_session=True 表示这个 session 是本函数创建的，应由本函数关闭
        if owns_session:
            session.close()
