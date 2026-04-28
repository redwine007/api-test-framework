import http_client
import pytest


@pytest.mark.smoke
def test_httpbin_get_returns_200(base_url, timeout_seconds, test_context):
    """
    - 发起 GET 请求
    - 断言状态码为 200

    """
    url = f"{base_url}/get"
    print(f"[DEBUG] base_url={base_url}, timeout={timeout_seconds}")

    # 发起请求（这里先直接用 requests，Day5 再改成复用 http_client）
    resp = http_client.http_get(url, timeout=timeout_seconds)

    # 断言：状态码必须等于 200，否则测试失败
    assert resp.status_code == 200, f"unexpected status code: {resp.status_code}"


@pytest.mark.regression
@pytest.mark.parametrize("path, expected_status",[
        ("/status/200", 200),
        ("/status/404", 404),
        ("/status/500", 500),
])
def test_httpbin_status_endpoints(base_url, timeout_seconds, path, expected_status):
    # 这个用例是“可预期的失败/错误码”
    # httpbin 的 /status/404 会稳定返回 404（对外部依赖的要求：稳定可复现）
    url = f"{base_url}{path}"

    res = http_client.http_get(url, timeout=timeout_seconds)

    assert res.status_code == expected_status, f"path={path}, 预期={expected_status}, 实际={res.status_code}"


def test_httpbin_headers_echo_contains_request_headers(base_url, timeout_seconds):
    """
    验证： headers ，httpbin 能把请求头回显在 JSON 里。
    """
    url = f"{base_url}/headers"
    resp = http_client.http_get(url, timeout=timeout_seconds, token="")

    assert resp.status_code == 200
    data = resp.json()
    # httpbin 返回结构里包含 "headers"
    assert "headers" in data

    # 进一步断言
    headers_echo = data["headers"]
    assert "Host" in headers_echo


@pytest.mark.regression
def test_bearer_endpoint_when_token_configured(base_url, timeout_seconds, bearer_token):
    if not bearer_token:
        pytest.skip("TEST_TOKEN 未配置，跳过 bearer 用例")
    url = f"{base_url}/bearer"
    resp = http_client.http_get(url, timeout=timeout_seconds, token=bearer_token)
    assert resp.status_code == 200