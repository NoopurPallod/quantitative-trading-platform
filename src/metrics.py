def calculate_metrics(data, final_value, initial_capital):

    return_pct = ((final_value - initial_capital) / initial_capital) * 100

    buy_price = data.iloc[0]["Close"]
    sell_price = data.iloc[-1]["Close"]

    buy_hold_return = ((sell_price - buy_price) / buy_price) * 100

    data["Running Max"] = data["Portfolio Value"].cummax()

    data["Drawdown"] = (data["Portfolio Value"] - data["Running Max"]) / data["Running Max"]

    max_drawdown = data["Drawdown"].min()

    data["Daily Return"] = data["Portfolio Value"].pct_change()

    daily_returns = data["Daily Return"].dropna()

    sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)

    return {
        "return_pct": return_pct,
        "buy_hold_return": buy_hold_return,
        "max_drawdown": max_drawdown,
        "sharpe_ratio": sharpe_ratio
    }