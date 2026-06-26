def run_backtest(data, initial_capital,verbose=False):

    cash = initial_capital
    shares = 0
    portfolio_values = []

    for index, row in data.iterrows():

        if row["Position"] == 1 and shares == 0:

            shares = cash // row["Close"]
            cash -= shares * row["Close"]
            if verbose:
                print("BUY", index.date(), "@", round(row["Close"], 2))

        elif row["Position"] == -1 and shares > 0:

            cash += shares * row["Close"]
            shares = 0

            if verbose:
                print("SELL", index.date(), "@", round(row["Close"], 2))

        portfolio_value = cash + shares * row["Close"]
        portfolio_values.append(portfolio_value)

    data["Portfolio Value"] = portfolio_values

    final_value = cash + shares * data.iloc[-1]["Close"]

    return data, final_value
