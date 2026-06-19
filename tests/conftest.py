# conftest.py — pytest 共通フィクスチャを定義する

import pytest

from analysis_titanic.load_data import load_train


@pytest.fixture
def train_df():
    return load_train()
