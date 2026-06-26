import yfinance as yf

def load_data(ticker, start, end):

    data = yf.download(
        ticker,
        start=start,
        end=end
    )

    data.columns = data.columns.get_level_values(0)

    return data