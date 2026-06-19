# ADR 0001: hatchling + src レイアウト

## 状況

Python パッケージ管理に uv を採用。分析コードの再利用とテスト容易性のため src レイアウトが必要。

## 決定

- build backend: **hatchling**
- パッケージ配置: `src/analysis_titanic/`
- `[tool.uv] package = true` で editable install

## 理由

- `ai-agent-devenv-template` と同一パターンで AI エージェント運用と整合
- ノートブックから `from analysis_titanic.load_data import load_train` が可能
- pytest の `pythonpath = ["src"]` と整合

## 影響

- `uv sync` でプロジェクト自体もインストールされる
- 新モジュール追加時は `doc/specs/05_ディレクトリ構成.md` を更新
