# uv 環境構築

## 初回

```powershell
# Windows
.\scripts\setup_env.ps1
```

```bash
# macOS / Linux
bash scripts/setup_env.sh
```

## 日常

```powershell
uv sync                  # 依存関係同期
uv add pandas            # パッケージ追加
uv run pytest tests/unit -v
uv run jupyter lab
```

## 注意

- `uv.lock` はコミットする
- `.venv/` は Git 除外（自動生成）
