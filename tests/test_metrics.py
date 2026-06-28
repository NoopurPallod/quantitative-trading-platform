import numpy as np
import pytest

from metrics import calculate_metrics


def test_calculate_metrics_returns_expected_portfolio_metrics():
    portfolio_history = [
        100000.0,
        101000.0,
        102000.0,
        104000.0,
        103000.0,
        105000.0,
        107000.0,
        106000.0
    ]

    data = {
        "Close": [100.0, 101.0, 102.0, 104.0, 103.0, 105.0, 107.0, 106.0],
        "Portfolio Value": portfolio_history
    }

    import pandas as pd

    frame = pd.DataFrame(data)
    metrics = calculate_metrics(frame.copy(), 106000.0, 100000.0)

    daily_returns = pd.Series(portfolio_history).pct_change().dropna()
    expected_sharpe = (
        daily_returns.mean() / daily_returns.std()
    ) * (252 ** 0.5)

    assert metrics["return_pct"] == 6.0
    assert metrics["buy_hold_return"] == 6.0
    assert metrics["max_drawdown"] == (103000.0 - 104000.0) / 104000.0
    assert metrics["sharpe_ratio"] == pytest.approx(expected_sharpe)
