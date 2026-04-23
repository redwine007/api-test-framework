import pytest


@pytest.fixture
def base_url():
    """
    基础域名
    """
    return "https://httpbin.org"


@pytest.fixture
def timeout_seconds():
    """
    统一超时时间，避免每个测试重复写数字
    """
    return 10