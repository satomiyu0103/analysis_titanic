# プロジェクトマップ（AIエージェント向け）

このプロジェクトは **Titanic 生存予測のデータ分析** です。
AI エージェントが短時間で要件・設計・運用ルールを把握できるように、参照先を整理しています。

> **行動規範**: [`.cursor/rules/agent_core.mdc`](../../.cursor/rules/agent_core.mdc) / [`.cursor/rules/agent_implement.mdc`](../../.cursor/rules/agent_implement.mdc)

## まず読むべき 4 ファイル（Phase 1）

1. `doc/ai_guidelines/Project_map.md` — このファイル
2. `doc/specs/02_要件定義.md` — 実装範囲（MoSCoW）
3. `doc/specs/04_機能一覧.md` — 全機能の実装状況
4. `doc/ai_guidelines/試験実装のエラー.md` — 既知エラー

---

## 機能コード体系（FR / NFR）

```
[TYPE]-[CATEGORY]-[NNN]

FR カテゴリ:
  DATA  = データ読込・前処理
  EDA   = 探索的分析・可視化
  MODEL = モデル構築・評価
  SUB   = 提出ファイル生成

NFR カテゴリ:
  SEC   = セキュリティ
  REPRO = 再現性
  OPS   = 運用・保守
```

---

## 主要パス

| パス | 責務 |
|---|---|
| `src/analysis_titanic/` | 再利用可能な Python コード |
| `notebooks/` | EDA・試行錯誤（確定コードは src へ移す） |
| `data/` | 学習・テスト CSV（コミット対象） |
| `models/` | 学習済みモデル（Git 除外） |
| `out/` | 提出 CSV・図表（Git 除外） |
| `tests/unit/` | 前処理・ユーティリティの単体テスト |
| `tests/integration/` | パイプライン結合テスト |
| `doc/specs/` | 要件・設計・CHANGELOG |

---

## AI エージェント向け参照ガイド

| やりたいこと | 参照先 |
|---|---|
| 要件確認 | `doc/specs/02_要件定義.md` |
| 機能コード・実装状況 | `doc/specs/04_機能一覧.md` |
| パイプライン設計 | `doc/specs/03_システム設計.md` |
| ディレクトリ構成 | `doc/specs/05_ディレクトリ構成.md` |
| 過去のエラー | `doc/ai_guidelines/試験実装のエラー.md` |
| 開発ルール | `doc/ai_guidelines/実装規約.md` |
| uv 環境構築 | `doc/reference/setup/uv.md` |
