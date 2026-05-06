# 在本地模拟 CI （安装依赖 -> pre-commit -> pytest）
# 遇到错误立即停止
$ErrorActionPreference = "Stop"

Write-Host "[1/3] install deps"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host "[2/3] pre-commit"
python -m pre_commit run --all-files

Write-Host "[3/3] pytest"
python -m pytest -q

Write-Host "DONE"
