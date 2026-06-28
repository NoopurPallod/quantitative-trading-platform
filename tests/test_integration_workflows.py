import pytest

import data_loader
from analyze import analyze_stock
from backtester import run_backtest
from data_loader import load_data
from metrics import calculate_metrics
from optimizer import optimize_parameters
from strategy import generate_signals


def test_data_loader_to_strategy_to_optimizer_workflow(monkeypatch, long_multi_index_download_frame):
    def fake_download(ticker, start, end, progress):
        return long_multi_index_download_frame.copy()

    monkeypatch.setattr(data_loader.yf, "download", fake_download)

    data = load_data("AAPL", "2022-01-01", "2025-01-01")
    signal_data = generate_signals(data.copy(), 2, 3)
    backtest_data, final_value = run_backtest(signal_data.copy(), 100000)
    metrics = calculate_metrics(backtest_data.copy(), final_value, 100000)
    optimized_results = optimize_parameters("AAPL")

    assert list(data.columns) == ["Close"]
    assert "Signal" in signal_data.columns
    assert "Portfolio Value" in backtest_data.columns
    assert metrics["return_pct"] == pytest.approx((final_value - 100000) / 100000 * 100)
    assert len(optimized_results) == 4
    assert {item["Short MA"] for item in optimized_results} == {20, 50}
    assert {item["Long MA"] for item in optimized_results} == {100, 200}


def test_analyze_stock_end_to_end_workflow(monkeypatch, long_multi_index_download_frame):
    def fake_download(ticker, start, end, progress):
        return long_multi_index_download_frame.copy()

    monkeypatch.setattr(data_loader.yf, "download", fake_download)

    result = analyze_stock("aapl")

    assert result["ticker"] == "AAPL"
    assert set(result) == {"ticker", "best_strategy", "all_strategies", "chart_data"}
    assert len(result["all_strategies"]) == 4
    assert result["best_strategy"] == max(
        result["all_strategies"],
        key=lambda item: item["Sharpe"]
    )
    assert len(result["chart_data"]) == 200
    assert set(result["chart_data"][0]) == {"date", "close", "ma_short", "ma_long"}
