from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
OUT_DIR = PROJECT_ROOT / "out"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

TRAIN_CSV = DATA_DIR / "train.csv"
TEST_CSV = DATA_DIR / "test.csv"
SAMPLE_SUBMIT_CSV = DATA_DIR / "sample_submit.csv"

TRAIN_COLUMNS = [
    "id",
    "survived",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]

TEST_COLUMNS = [
    "id",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]
