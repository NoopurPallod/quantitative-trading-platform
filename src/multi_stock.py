from optimizer import optimize_parameters

stocks = [
    "AAPL",
    "MSFT",
    "GOOG"
]
for stock in stocks:

    results = optimize_parameters(stock)

    best_strategy = max(
        results,
        key=lambda x: x["Sharpe"]
    )

    print(stock)

    print(
        f"Best Strategy: "
        f"MA{best_strategy['Short MA']}/"
        f"MA{best_strategy['Long MA']}"
    )

    print(
        f"Return: "
        f"{best_strategy['Return']}%"
    )

    print(
        f"Sharpe: "
        f"{best_strategy['Sharpe']}"
    )