# API Test Framework

一个基于 Python + pytest 的接口自动化测试项目，支持基础冒烟回归、环境变量配置、测试报告和 CI 自动执行。

---

## 1. 项目目标

- 用最小工程化结构搭建接口自动化测试框架
- 支持 smoke / regression 分层执行
- 支持环境变量配置（.env）
- 支持本地 HTML 报告与 GitHub Actions 自动执行

---

## 2. 技术栈

- Python 3.10
- pytest
- requests
- python-dotenv
- pytest-html
- GitHub Actions（CI）

---

## 3. 目录结构

```text
api-test-framework/
├─ tests/                    # 测试用例
├─ conftest.py               # pytest fixture（共享前后置、公共配置注入）
├─ http_client.py            # HTTP 请求封装（含重试）
├─ config.py                 # 配置读取入口（.env + 默认值）
├─ pytest.ini                # pytest 配置（路径、标签等）
├─ requirements.txt          # 依赖清单
├─ .env.example              # 环境变量模板（可提交）
└─ .github/workflows/ci.yml  # GitHub Actions CI
```

---

## 4. 快速开始

### 4.1 创建虚拟环境并安装依赖
```python
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 4.2 配置环境变量
复制 .env.example 为 .env，并填写：
```python
TEST_BASE_URL=https://httpbin.org
TEST_TIMEOUT=5
```

### 4.3 运行测试
```python
python -m pytest -q
```

### 4.4 运行冒烟测试
```python
python -m pytest -q -m smoke
```

### 4.5 生成 HTML 报告
```python
python -m pytest -q --html=reports/report.html --self-contained-html
```

## 5. 当前能力
- 用 @pytest.mark.smoke / @pytest.mark.regression 做测试分层
- 用 @pytest.mark.parametrize 做参数化测试，减少重复代码
- 用 fixture 实现 setup/teardown，统一前后置流程
- 用 python-dotenv + os.getenv 实现环境配置解耦
- 请求层封装基础重试，降低网络抖动带来的偶发失败
- 接入 GitHub Actions，实现 push/PR 自动执行测试

## 6. 后续规划
- 增加接口鉴权与公共请求头封装
- 增加失败截图/日志增强（如 trace_id）
- 增加 Allure 报告
- 增加 nightly regression 任务