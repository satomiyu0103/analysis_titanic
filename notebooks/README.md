# notebooks

分析用 Jupyter ノートブック。**番号順**に進めてください。

中身のコードは **自分で書く** 想定です。各ファイルにはやることとヒントだけ書いてあります。

| ファイル | 内容 |
|---|---|
| [01_eda.ipynb](01_eda.ipynb) | データの中身・欠損・生存率の可視化（EDA） |
| [02_baseline_model.ipynb](02_baseline_model.ipynb) | 前処理 + ベースラインモデル学習・保存 |
| [03_submission.ipynb](03_submission.ipynb) | テストデータ予測 → `out/submission.csv` |

## 起動方法

```powershell
uv run jupyter lab
```

カーネルは `.venv` の Python を選びます。

## 出力先（02・03 で使う）

- モデル: `models/baseline_model.joblib`（Git 除外）
- 提出: `out/submission.csv`（Git 除外）

## 困ったとき

- データ読込: `src/analysis_titanic/load_data.py` の `load_train()` / `load_test()`
- 列の意味: `01_eda.ipynb` の表を参照
- 環境: [doc/reference/setup/uv.md](../doc/reference/setup/uv.md)
