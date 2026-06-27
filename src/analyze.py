from optimizer import optimize_parameters
from data_loader import load_data
from strategy import generate_signals


def analyze_stock(ticker):

    results = optimize_parameters(ticker)

    results.sort(
        key=lambda x: x["Sharpe"],
        reverse=True
    )

    best_strategy = max(
        results,
        key=lambda x: x["Sharpe"]
    )

    print("Reached here")

    data = load_data(
        ticker,
        "2022-01-01",
        "2025-01-01"
    )

    data = generate_signals(
        data,
        best_strategy["Short MA"],
        best_strategy["Long MA"]
    )

    chart_data = []

    for index, row in data.tail(200).iterrows():

        chart_data.append({

            "date": str(index.date()),

            "close": float(row["Close"]),

            "ma_short": float(
                row[f"MA{best_strategy['Short MA']}"]
            ),

            "ma_long": float(
                row[f"MA{best_strategy['Long MA']}"]
            )

        })

    return {
        "ticker": ticker,
        "best_strategy": best_strategy,
        "all_strategies": results,
        "chart_data": chart_data
    }