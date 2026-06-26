from data_loader import load_data
from strategy import generate_signals
from backtester import run_backtest
from metrics import calculate_metrics
from visualization import plot_portfolio

data = load_data("AAPL", "2022-01-01", "2025-01-01")

data = generate_signals(data, 50, 200)

data, final_value = run_backtest(data, 100000)

results = calculate_metrics(data, final_value, 100000)
print(f"Return: {results['return_pct']:.2f}%")
print(f"Buy & Hold: {results['buy_hold_return']:.2f}%")
print(f"Max Drawdown: {results['max_drawdown'] * 100:.2f}%")
print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")

plot_portfolio(data)