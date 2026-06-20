# analysis-titanic

Titanic 生存予測のデータ分析プロジェクト（uv + src レイアウト）

## クイックスタート

```powershell
# 初回
.\scripts\setup_env.ps1

# テスト
uv run pytest tests/unit -v

# Jupyter
uv run jupyter lab
```

`config/.env.example` を `config/.env` にコピーして設定する（任意）。

---

## ディレクトリ

| パス | 用途 |
|---|---|
| `src/analysis_titanic/` | 再利用可能な Python コード |
| `notebooks/` | EDA・試行錯誤 |
| `data/` | train.csv / test.csv |
| `models/` | 学習済みモデル（Git 除外） |
| `out/` | 提出 CSV・図表（Git 除外） |
| `doc/` | 要件・設計・エージェントガイド |

---

## ドキュメント

### for user

| ファイル | 内容 |
|---|---|
| [doc/reference/getting-started/入門ガイド.md](doc/reference/getting-started/入門ガイド.md) | フォルダの意味 |
| [doc/reference/setup/uv.md](doc/reference/setup/uv.md) | uv 環境 |
| [doc/specs/02_要件定義.md](doc/specs/02_要件定義.md) | 要件 |
| [doc/specs/06_ROADMAP.md](doc/specs/06_ROADMAP.md) | 実装計画 |
| [doc/specs/08_分析状況.md](doc/specs/08_分析状況.md) | **分析の現状と次のステップ** |

### for ai

| ファイル | 内容 |
|---|---|
| [AGENTS.md](AGENTS.md) | クイックリファレンス |
| [.cursor/rules/agent_core.mdc](.cursor/rules/agent_core.mdc) | 常時ルール |
| [doc/ai_guidelines/Project_map.md](doc/ai_guidelines/Project_map.md) | 参照先一覧 |

---

## 開発コマンド

```powershell
uv sync
uv run pytest tests/unit -v
uv run pytest tests/integration -v
uv run jupyter lab
```
