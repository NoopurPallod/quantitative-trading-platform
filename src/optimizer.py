from data_loader import load_data
from strategy import generate_signals
from backtester import run_backtest
from metrics import calculate_metrics


def optimize_parameters(ticker):

    results = []

    short_windows = [20, 50]
    long_windows = [100, 200]
    data = load_data(
                ticker,
                "2022-01-01",
                "2025-01-01"
            )

    for short_window in short_windows:

        for long_window in long_windows:

            

            data = generate_signals(
                data,
                short_window,
                long_window
            )

            data, final_value = run_backtest(
                data,
                100000
            )

            metrics = calculate_metrics(
                data,
                final_value,
                100000
            )

            results.append({
                "Short MA": short_window,
                "Long MA": long_window,
                "Return": round(metrics["return_pct"], 2),
                "Sharpe": round(metrics["sharpe_ratio"], 2)
            })
    

    return results