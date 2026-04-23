import http_client


def test_httpbin_get_returns_200():
    """
    - 发起 GET 请求
    - 断言状态码为 200

    """
    url = "https://httpbin.org/get"
    timeout = 5

    # 发起请求（这里先直接用 requests，Day5 再改成复用 http_client）
    resp = http_client.http_get(url, timeout=timeout)

    # 断言：状态码必须等于 200，否则测试失败
    assert resp.status_code == 200, f"unexpected status code: {resp.status_code}"


def test_httpbin_status_404():
    # 这个用例是“可预期的失败/错误码”
    # httpbin 的 /status/404 会稳定返回 404（对外部依赖的要求：稳定可复现）
    url = "https://httpbin.org/status/404"
    timeout = 5

    res = http_client.http_get(url, timeout=timeout)

    assert res.status_code == 404,f"expected 404, got: {res.status_code}"