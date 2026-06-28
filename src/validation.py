import re


MAX_PORTFOLIO_SIZE = 4
TICKER_PATTERN = re.compile(r"^[A-Z][A-Z0-9.-]{0,9}$")


def normalize_ticker(ticker):
    if not isinstance(ticker, str):
        raise ValueError("Ticker must be a string.")

    normalized_ticker = ticker.strip().upper()

    if not normalized_ticker:
        raise ValueError("Ticker must not be empty.")

    if not TICKER_PATTERN.fullmatch(normalized_ticker):
        raise ValueError("Ticker format is invalid.")

    return normalized_ticker


def validate_stock_list(stocks):
    if not isinstance(stocks, list):
        raise ValueError("Stocks must be provided as a list.")

    normalized_stocks = [
        normalize_ticker(stock)
        for stock in stocks
    ]

    if not normalized_stocks:
        raise ValueError("At least one stock ticker is required.")

    if len(normalized_stocks) > MAX_PORTFOLIO_SIZE:
        raise ValueError(
            f"A portfolio can contain at most {MAX_PORTFOLIO_SIZE} stocks."
        )

    if len(set(normalized_stocks)) != len(normalized_stocks):
        raise ValueError("Duplicate stock tickers are not allowed.")

    return normalized_stocks
