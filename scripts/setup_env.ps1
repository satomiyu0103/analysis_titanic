# Windows PowerShell 用: プロジェクトルートで実行するセットアップスクリプト
# 実行例: .\scripts\setup_env.ps1

param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location (Resolve-Path "$scriptDir\..").Path

if (-not (Test-Path pyproject.toml)) {
    Write-Error "pyproject.toml が見つかりません。プロジェクトルートで実行してください。"
    exit 1
}

Write-Host "Upgrading pip and installing uv..."
python -m pip install --upgrade pip
python -m pip install uv

Write-Host "Syncing dependencies..."
uv sync --all-groups

Write-Host "Done. Commit uv.lock after adding dependencies."
