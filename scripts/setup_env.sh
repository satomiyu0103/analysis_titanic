#!/usr/bin/env bash
set -euo pipefail
# Run from repo root: bash scripts/setup_env.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

if [ ! -f pyproject.toml ]; then
  echo "pyproject.toml not found. Run from project root." >&2
  exit 1
fi

python -m pip install --upgrade pip
python -m pip install uv || true

uv sync --all-groups

echo "Done. Commit uv.lock after adding dependencies."
