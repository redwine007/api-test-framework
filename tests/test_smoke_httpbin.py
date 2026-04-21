import requests


def test_httpbin_get_returns_200():
    """
    - 发起 GET 请求
    - 断言状态码为 200

    """
    url = "https://httpbin.org/get"
    timeout = 5

    # 发起请求（这里先直接用 requests，Day5 再改成复用 http_client）
    resp = requests.get(url, timeout=timeout)

    # 断言：状态码必须等于 200，否则测试失败
    assert resp.status_code == 200, f"unexpected status code: {resp.status_code}"