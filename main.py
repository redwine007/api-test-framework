# 把“配置 + 请求 + 判断”串起来，并输出退出码给 CI/CD。

import sys  # 标准库：用于退出码（也可以继续用 SystemExit，这里用 sys.exit ）

import config
import http_client


def assert_status_ok(response) -> bool:
    """
    最小断言：状态码是否为 200。

    """
    print(f"[INFO] url={response.url}")
    print(f"[INFO] status_code={response.status_code}")

    if response.status_code == 200:
        print("[PASS] status code is 200")
        return True

    print("[FAIL] unexpected status code")
    return False


if __name__ == "__main__":
    # 1) 从配置读取参数
    url = config.get_base_url()
    timeout = config.get_timeout_seconds()

    # 2) 发起请求
    try:
        resp = http_client.http_get(url, timeout)
    except Exception as e:
        print(f"[ERROR] request failed: {e}")
        sys.exit(1)

    # 3) 断言判断
    ok = assert_status_ok(resp)

    # 4) 退出码：0 成功，1 失败
    sys.exit(0 if ok else 1)
