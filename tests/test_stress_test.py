import pytest

from stress_test import stress_test


def test_stress_test_calculates_weighted_portfolio_loss():
    portfolio_loss_pct, stressed_value, loss = stress_test(
        ["AAPL", "MSFT"],
        [0.6, 0.4],
        {"AAPL": -0.2, "MSFT": -0.1},
        100000
    )

    assert portfolio_loss_pct == pytest.approx(-0.16)
    assert stressed_value == pytest.approx(84000.0)
    assert loss == pytest.approx(16000.0)
