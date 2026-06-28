import yfinance as yf
import pandas as pd

from validation import normalize_ticker

def load_data(ticker, start, end):
    normalized_ticker = normalize_ticker(ticker)

    data = yf.download(
        normalized_ticker,
        start=start,
        end=end,
        progress=False
    )

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    if data.empty or "Close" not in data.columns:
        raise ValueError(
            f"No historical data found for ticker '{normalized_ticker}'."
        )

    return data.sort_index()
