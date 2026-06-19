# CHANGELOG

形式は [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づく。
機能コードの詳細は [04_機能一覧.md](04_機能一覧.md) を参照。

---

## [Unreleased]

### Added

- `chore` テンプレート `ai-agent-devenv-template` を参考にリポジトリ構成を整備（FR-DATA-001）
- `src/analysis_titanic/` — パス定数・CSV 読込モジュール（FR-DATA-001）
- `tests/unit/test_load_data.py` — データ読込の unit test（FR-DATA-001）
- `doc/` — specs / ai_guidelines / reference / adr
- `.cursor/rules/` — agent_core / agent_implement
- `config/.env.example` — 実行時設定テンプレート
- `scripts/setup_env.ps1` / `setup_env.sh` — 初回セットアップ

### Changed

- `pyproject.toml` — hatchling + src レイアウト + dev 依存（pytest, ruff）
- `.gitignore` — DS 向け（data/ はコミット可、models/ out/ は除外）

---

## 記法ガイド

```
### Added / Changed / Fixed
- 説明（FR-XXX-NNN）
```
