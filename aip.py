import requests


def api_run():
    url = 'https://httpbin.org/get'
    res = requests.get(url, timeout=10)
    print('code:', res.status_code)
    try:
        data = res.json()
    except requests.exceptions.JSONDecodeError:
        print('response is not json:', res.text[:200])
        return
    print('res_url:', data.get('url'))


if __name__ == '__main__':
    api_run()
