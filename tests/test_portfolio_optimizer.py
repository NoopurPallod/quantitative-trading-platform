import numpy as np
import pandas as pd
import pytest

import portfolio_optimizer
from portfolio_optimizer import (
    calculate_portfolio_performance,
    optimize_portfolio,
)


def test_calculate_portfolio_performance_returns_expected_values(expected_portfolio_performance):
    returns, weights = expected_portfolio_performance

    portfolio_return, portfolio_volatility, sharpe_ratio = calculate_portfolio_performance(
        returns,
        weights
    )

    expected_return = np.sum(returns.mean() * weights) * 252
    expected_volatility = np.sqrt(
        np.dot(weights.T, np.dot(returns.cov() * 252, weights))
    )
    expected_sharpe = (expected_return - 0.05) / expected_volatility

    assert portfolio_return == pytest.approx(expected_return)
    assert portfolio_volatility == pytest.approx(expected_volatility)
    assert sharpe_ratio == pytest.approx(expected_sharpe)


def test_optimize_portfolio_returns_expected_shape(monkeypatch, multi_asset_price_map):
    def fake_load_data(ticker, start, end):
        return multi_asset_price_map[ticker].copy()

    monkeypatch.setattr(portfolio_optimizer, "load_data", fake_load_data)

    result = optimize_portfolio(["AAPL", "MSFT"])

    assert set(result) == {"weights", "return", "volatility", "sharpe", "var", "stress_tests"}
    assert set(result["weights"]) == {"AAPL", "MSFT"}
    assert pytest.approx(sum(result["weights"].values()), rel=0, abs=0.05) == 100.0
    assert len(result["stress_tests"]) == 3
    assert {item["Scenario"] for item in result["stress_tests"]} == {
        "Market Crash",
        "Severe Crash",
        "Random Stress"
    }


def test_optimize_portfolio_supports_single_stock_boundary(monkeypatch, multi_asset_price_map):
    def fake_load_data(ticker, start, end):
        return multi_asset_price_map[ticker].copy()

    monkeypatch.setattr(portfolio_optimizer, "load_data", fake_load_data)

    result = optimize_portfolio(["AAPL"])

    assert result["weights"] == {"AAPL": 100.0}
    assert len(result["stress_tests"]) == 3


def test_optimize_portfolio_supports_maximum_portfolio_size(monkeypatch, multi_asset_price_map):
    def fake_load_data(ticker, start, end):
        return multi_asset_price_map[ticker].copy()

    monkeypatch.setattr(portfolio_optimizer, "load_data", fake_load_data)

    result = optimize_portfolio(["AAPL", "MSFT", "GOOG", "TSLA"])

    assert len(result["weights"]) == 4
    assert pytest.approx(sum(result["weights"].values()), rel=0, abs=0.1) == 100.0


@pytest.mark.parametrize(
    "stocks",
    [
        [],
        ["AAPL", "MSFT", "GOOG", "TSLA", "NFLX"],
        ["AAPL", "AAPL"]
    ]
)
def test_optimize_portfolio_rejects_invalid_portfolio_lists(stocks):
    with pytest.raises(ValueError):
        optimize_portfolio(stocks)
