import pandas as pd

from analysis_titanic.paths import TEST_COLUMNS, TEST_CSV, TRAIN_COLUMNS, TRAIN_CSV


def load_train() -> pd.DataFrame:
    """学習データを読み込む。"""
    df = pd.read_csv(TRAIN_CSV)
    missing = set(TRAIN_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"train.csv に不足列があります: {sorted(missing)}")
    return df


def load_test() -> pd.DataFrame:
    """テストデータを読み込む。"""
    df = pd.read_csv(TEST_CSV)
    missing = set(TEST_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"test.csv に不足列があります: {sorted(missing)}")
    return df
