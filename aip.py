import requests


def smoke_check(url: str, timeout: int = 5) -> bool:
    """
    最小探针函数：
    - url: 要请求的地址
    - timeout: 超时时间（秒）
    - 返回值：True=通过，False=失败
    """
    try:
        response = requests.get(url, timeout=timeout)

        print(f"[INFO] url={url}")
        print(f"[INFO] status_code={response.status_code}")

        # 这里先用最简单规则：状态码是 200 就算通过
        if response.status_code == 200:
            print("[PASS] smoke check passed")
            return True

        print("[FAIL] smoke check failed: unexpected status code")
        return False

    except requests.RequestException as e:
        # 所有 requests 相关网络异常都在这里处理
        print(f"[ERROR] request failed: {e}")
        return False


if __name__ == "__main__":
    target_url = "https://httpbin.org/get"
    result = smoke_check(target_url)

    # 给 shell 返回明确退出码：0=成功，1=失败（CI 会用到）
    raise SystemExit(0 if result else 1)