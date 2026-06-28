import numpy as np

from risk_metrics import calculate_var


def test_calculate_var_uses_requested_confidence_level(portfolio_returns_series):
    result = calculate_var(portfolio_returns_series, confidence_level=95)

    assert result == np.percentile(portfolio_returns_series, 5)
