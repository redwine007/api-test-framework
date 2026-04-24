# 目标：作为项目唯一配置入口。
# 规则：优先读取环境变量；没有则使用默认值。

import os
from dotenv import load_dotenv

# 启动时加载 .env（如果文件不存在，不会报错）
load_dotenv()

# 默认值常量（集中管理，避免散落）
DEFAULT_BASE_URL = "https://httpbin.org"
DEFAULT_TIMEOUT_SECONDS = 8


def get_base_url() -> str:
    """
    获取基础地址：
    - 优先读取环境变量 TEST_BASE_URL
    - 未设置时使用默认值 DEFAULT_BASE_URL
    """
    return os.getenv("TEST_BASE_URL", DEFAULT_BASE_URL)


def get_timeout_seconds() -> int:
    """
    获取超时时间：
    - 优先读取环境变量 TEST_TIMEOUT（字符串）
    - 未设置时用默认值
    - 最终转成 int，供 requests 使用
    """
    value = os.getenv("TEST_TIMEOUT", str(DEFAULT_TIMEOUT_SECONDS))
    return int(value)