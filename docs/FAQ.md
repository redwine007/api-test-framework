```markdown
# FAQ
## 1) 为什么 `.env.example` 写了变量但程序读不到？
`.env.example` 是模板，默认不会自动加载。请复制为 `.env` 后再运行。
## 2) 为什么 CI 报 requirements 编码错误？
`requirements.txt` 必须是 UTF-8。PowerShell 重定向可能生成 UTF-16，请用编辑器或 `Set-Content -Encoding utf8` 重建。
## 3) pytest 收集不到用例？
检查命名 `test_*.py`、运行目录是否在项目根、`pytest.ini` 配置是否正确。
## 4) pre-commit 第一次失败但显示 modified？
这是自动修复，请 `git add` 后再 `git commit`。
## 5) GitHub Actions 不触发？
检查 workflow 的 `branches` 是否与实际主分支一致（master/main）。
```
