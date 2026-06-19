import pandas as pd
import pytest

from analysis_titanic.load_data import load_test, load_train


def test_load_train_returns_expected_columns():
    df = load_train()
    assert list(df.columns) == [
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


def test_load_train_has_rows():
    df = load_train()
    assert len(df) > 0


def test_load_test_returns_expected_columns():
    df = load_test()
    assert "survived" not in df.columns
    assert "id" in df.columns


def test_load_test_has_rows():
    df = load_test()
    assert len(df) > 0
