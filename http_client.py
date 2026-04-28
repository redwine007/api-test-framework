# 封装 HTTP 请求细节。
# 业务判断不要和 requests 细节耦合，后面好替换/好测试。
import time

import requests

import uuid


def _default_headers() -> dict:
    """
    统一公共请求头
    """
    return {
        "X-Request-Id": str(uuid.uuid4()),  # 一次请求一个唯一 ID
        "Content-Type": "application/json",
    }


def _auth_header(token: str) -> dict:
    """
    有 token 才加认证头，避免没配置时硬塞无效值
    """
    if not token:
        return {}
    return {"Authorization": f"Bearer {token}"}


def http_get(
        url: str,
        timeout: int,
        token: str = "",
        retries: int = 2,
        retry_interval: float = 0.5
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

    headers = {**_default_headers(), **_auth_header(token)}
    err_info = None
    for attempt in range(retries + 1):
        try:
            return requests.get(url, timeout=timeout, headers=headers)
        except requests.RequestException as e:
            err_info = e
            if attempt < retries:
                time.sleep(retry_interval)
            else:
                raise err_info
