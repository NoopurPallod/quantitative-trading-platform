from data_loader import load_data
from strategy import generate_signals
from backtester import run_backtest
from metrics import calculate_metrics
from visualization import plot_portfolio
from optimizer import optimize_parameters
results = optimize_parameters()
results.sort(
    key=lambda x: x["Sharpe"],
    reverse=True
)
for result in results:

    print(
        f"MA{result['Short MA']}/MA{result['Long MA']} | "
        f"Return: {result['Return']}% | "
        f"Sharpe: {result['Sharpe']}"
    )
best_strategy = max(results,key=lambda x: x["Sharpe"])
print("\nBest Strategy")
print(f"MA{best_strategy['Short MA']}/"f"MA{best_strategy['Long MA']}")
print(f"Return: {best_strategy['Return']}%")
print(f"Sharpe: {best_strategy['Sharpe']}")