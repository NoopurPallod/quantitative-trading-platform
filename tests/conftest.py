import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"

for path in (PROJECT_ROOT, SRC_ROOT):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)


@pytest.fixture
def price_data():
    index = pd.date_range("2024-01-01", periods=8, freq="D")
    close_prices = [100.0, 101.0, 102.0, 104.0, 103.0, 105.0, 107.0, 106.0]

    return pd.DataFrame(
        {
            "Close": close_prices
        },
        index=index
    )


@pytest.fixture
def multi_asset_price_map():
    index = pd.date_range("2024-01-01", periods=8, freq="D")

    return {
        "AAPL": pd.DataFrame(
            {
                "Close": [100.0, 101.0, 102.5, 103.0, 104.5, 105.0, 106.0, 107.0]
            },
            index=index
        ),
        "MSFT": pd.DataFrame(
            {
                "Close": [200.0, 201.0, 201.5, 202.5, 203.0, 204.0, 205.5, 206.0]
            },
            index=index
        ),
        "GOOG": pd.DataFrame(
            {
                "Close": [300.0, 299.5, 301.0, 302.0, 303.5, 305.0, 306.0, 307.5]
            },
            index=index
        ),
        "TSLA": pd.DataFrame(
            {
                "Close": [150.0, 151.5, 153.0, 152.0, 154.0, 155.5, 157.0, 158.0]
            },
            index=index
        )
    }


@pytest.fixture
def multi_index_download_frame(price_data):
    frame = price_data.copy()
    frame.columns = pd.MultiIndex.from_product(
        [["Close"], ["AAPL"]]
    )
    return frame


@pytest.fixture
def long_multi_index_download_frame():
    index = pd.date_range("2023-01-01", periods=260, freq="D")
    trend = np.linspace(100.0, 160.0, num=260)
    seasonal = np.sin(np.linspace(0, 18, num=260)) * 3
    frame = pd.DataFrame(
        {
            "Close": trend + seasonal
        },
        index=index
    )
    frame.columns = pd.MultiIndex.from_product(
        [["Close"], ["AAPL"]]
    )
    return frame


@pytest.fixture
def portfolio_returns_series():
    return pd.Series(
        [-0.03, -0.01, 0.0, 0.015, 0.02, 0.03],
        name="portfolio_returns"
    )


@pytest.fixture
def expected_portfolio_performance():
    returns = pd.DataFrame(
        {
            "AAPL": [0.01, 0.015, -0.005, 0.02],
            "MSFT": [0.008, 0.012, 0.002, 0.011]
        }
    )
    weights = np.array([0.6, 0.4])
    return returns, weights
