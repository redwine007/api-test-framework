# 封装 HTTP 请求细节。
# 业务判断不要和 requests 细节耦合，后面好替换/好测试。

import requests


def http_get(url: str, timeout: int) -> requests.Response:
    """
    发送 GET 请求并返回 Response 对象。

    参数：
    - url: 请求地址
    - timeout: 超时时间（秒）

    返回：
    - requests.Response：包含 status_code、headers、text/json 等
    """
    # requests.get 会真正发起网络请求
    return requests.get(url, timeout=timeout)