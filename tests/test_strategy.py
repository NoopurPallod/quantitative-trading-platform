import numpy as np
import pandas as pd
import pytest

from strategy import generate_signals


def test_generate_signals_creates_expected_moving_average_columns(price_data):
    result = generate_signals(price_data.copy(), 2, 3)

    expected_short = pd.Series(
        [np.nan, 100.5, 101.5, 103.0, 103.5, 104.0, 106.0, 106.5],
        index=price_data.index,
        name="MA2"
    )
    expected_long = pd.Series(
        [np.nan, np.nan, 101.0, 102.3333333333, 103.0, 104.0, 105.0, 106.0],
        index=price_data.index,
        name="MA3"
    )

    pd.testing.assert_series_equal(result["MA2"], expected_short)
    pd.testing.assert_series_equal(
        result["MA3"],
        expected_long,
        check_exact=False,
        atol=1e-10
    )
    assert result["Signal"].tolist() == [0, 0, 1, 1, 1, 0, 1, 1]
    assert np.isnan(result["Position"].iloc[0])
    assert result["Position"].iloc[2] == 1


@pytest.mark.parametrize(
    ("short_window", "long_window"),
    [
        (1, 2),
        (7, 8)
    ]
)
def test_generate_signals_handles_boundary_windows(price_data, short_window, long_window):
    result = generate_signals(price_data.copy(), short_window, long_window)

    assert f"MA{short_window}" in result.columns
    assert f"MA{long_window}" in result.columns
    assert len(result) == len(price_data)
    assert set(result["Signal"].dropna().unique()).issubset({0, 1})
