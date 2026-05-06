# API Test Framework

一个基于 Python + pytest 的接口自动化测试项目，支持基础冒烟回归、环境变量配置、测试报告和 CI 自动执行。

---

## 1. 项目目标

- 用最小工程化结构搭建接口自动化测试框架
- 支持 smoke / regression 分层执行
- 支持环境变量配置（.env）
- 支持本地报告与 CI 自动执行，形成提交即验证的最小闭环

---

## 2. 技术栈

- ` Python` 3.10+（建议与 CI 对齐）
- `pytest`：测试运行与断言
- `requests`：HTTP 调用
- `python-dotenv`：加载 `.env` 到进程环境变量
- `jsonschema`：响应 JSON 的最小契约校验（可选增强）
- `pytest-html`：HTML 报告（可选）
- `allure-pytest` + Allure CLI：Allure 报告（可选）
- `pre-commit` + `ruff`：本地与 CI 代码质量门
- GitHub Actions：CI
---

## 3. 目录结构


```text
api-test-framework/
├─ tests/                         # pytest 用例（test_*.py）
├─ conftest.py                    # pytest fixture：共享配置注入、前后置等
├─ http_client.py                 # HTTP 客户端封装：默认 headers、可选 Bearer、重试、Session
├─ config.py                      # 配置统一入口：读取环境变量并提供默认值
├─ main.py
├─ pytest.ini                     # pytest 配置：testpaths、markers、pythonpath 等
├─ requirements.txt               # 依赖锁定（必须是 UTF-8）
├─ .env.example                   # 环境变量模板
├─ .env                           # 本地真实配置（不提交仓库；从模板复制生成）
├─ .pre-commit-config.yaml        # pre-commit hooks 配置
├─ .github/workflows/ci.yml       # GitHub Actions CI
├─ scripts/                       # 一键脚本（可选，但推荐）
│  └─ run_ci_local.ps1            # 本地模拟 CI：安装依赖 -> pre-commit -> pytest
├─ docs/
│  └─ FAQ.md                      # 常见问题（强烈建议维护）
├─ reports/                       # pytest-html 报告输出（运行产物，通常忽略提交）
├─ allure-results/                # Allure 原始结果（运行产物，通常忽略提交）
└─ allure-report/                 # Allure 生成报告（运行产物，通常忽略提交）
```

---

## 4. 快速开始
###  4.0 克隆与进入目录
```python
git clone https://github.com/redwine007/api-test-framework.git
cd api-test-framework
```

### 4.1 创建虚拟环境并安装依赖
#### PowerShell：
```python
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
#### Git Bash：
```python
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4.2 配置环境变量
#### .env.example 是模板，默认不会自动生效。请复制为 .env：

#### PowerShell：
```python
Copy-Item .env.example .env
```
#### Git Bash：
```python
cp .env.example .env
```

### 4.3 运行测试
```python
python -m pytest -q
```

### 4.4 运行冒烟测试
```python
python -m pytest -q -m smoke
```

### 4.5 生成 HTML 报告（可选）
```python
python -m pytest -q --html=reports/report.html --self-contained-html
```

### 4.6 生成 Allure 原始结果（可选）
```python
python -m pytest -q --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

### 4.7 一键脚本/本地CI（推荐 PowerShell）
```python
powershell -ExecutionPolicy Bypass -File .\scripts\run_ci_local.ps1
```

## 5. 当前能力
### 测试执行与分层
- 基于 pytest 的自动化用例组织与断言
- @pytest.mark.smoke / @pytest.mark.regression：按标签筛选执行，支持 PR 快速门禁与回归扩展
- @pytest.mark.parametrize：参数化减少重复用例

### 工程结构与可维护性
- http_client：HTTP 调用集中封装（便于统一超时/重试/headers/鉴权策略演进）
- config.py：配置读取集中入口，避免散落魔法数字与硬编码 URL
- conftest.py：fixture 共享配置与前后置

### 环境配置与多环境切换
- .env：本地真实配置（不用于提交）
- .env.example：模板，明确项目配置变量
- python-dotenv + os.getenv：支持默认值与环境覆盖（终端/CI 注入优先级更高）
-
### 契约与断言能力
- 基础断言：status_code、关键字段断言
- jsonschema：对响应 JSON 做最小结构契约校验（按项目是否已接入为准）

### 可观测性与报告
- 请求维度 X-Request-Id（或同类 trace 标识）用于排障串联（按需求为准）
- pytest-html：生成可读 HTML 报告（可选）
- allure-pytest：生成 Allure 原始结果，配合 Allure CLI 打开报告（可选）

### 质量门禁与 CI
- pre-commit：提交前自动检查与自动修复（行尾空格、EOF、YAML、ruff/ruff-format）
- GitHub Actions：push/PR 自动安装依赖并执行测试（并建议与本地 pre-commit 对齐

### 文档化与可复现
- docs/FAQ.md：FAQ
- scripts/run_ci_local.ps1：本地一键模拟 CI（可选）
## 6. 常见问题（FAQ）
常见问题请看：[docs/FAQ.md](docs/FAQ.md)
