import pytest
from fastapi.testclient import TestClient

import backend.main as api_main


@pytest.fixture
def client(monkeypatch, multi_asset_price_map):
    def fake_analyze_stock(ticker):
        normalized_ticker = ticker.strip().upper()
        if normalized_ticker == "INVALID123":
            raise ValueError("No historical data found for ticker 'INVALID123'.")

        return {
            "ticker": normalized_ticker,
            "best_strategy": {
                "Short MA": 20,
                "Long MA": 100,
                "Return": 12.34,
                "Sharpe": 1.56
            },
            "all_strategies": [
                {
                    "Short MA": 20,
                    "Long MA": 100,
                    "Return": 12.34,
                    "Sharpe": 1.56
                }
            ],
            "chart_data": [
                {
                    "date": "2024-01-01",
                    "close": 100.0,
                    "ma_short": 100.0,
                    "ma_long": 100.0
                }
            ]
        }

    def fake_optimize_portfolio(stocks):
        normalized_stocks = [stock.strip().upper() for stock in stocks]
        if not normalized_stocks:
            raise ValueError("At least one stock ticker is required.")
        if len(normalized_stocks) > 4:
            raise ValueError("A portfolio can contain at most 4 stocks.")

        return {
            "weights": {
                stock: round(100 / len(normalized_stocks), 2)
                for stock in normalized_stocks
            },
            "return": 14.25,
            "volatility": 18.1,
            "sharpe": 0.79,
            "var": -1.85,
            "stress_tests": [
                {
                    "Scenario": "Market Crash",
                    "Loss %": -20.0,
                    "Portfolio Value": 80000.0,
                    "Loss Amount": 20000.0
                }
            ]
        }

    monkeypatch.setattr(api_main, "analyze_stock", fake_analyze_stock)
    monkeypatch.setattr(api_main, "optimize_portfolio", fake_optimize_portfolio)

    return TestClient(api_main.app)


def test_get_root_returns_api_health_message(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Trading Platform API Running"}


def test_get_analyze_returns_analysis_for_valid_ticker(client):
    response = client.get("/analyze", params={"ticker": "AAPL"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["ticker"] == "AAPL"
    assert payload["best_strategy"]["Short MA"] == 20


@pytest.mark.parametrize(
    ("ticker", "expected_status"),
    [
        ("AAPL", 200),
        ("INVALID123", 400),
        ("", 400)
    ]
)
def test_get_analyze_equivalence_partitions(client, ticker, expected_status):
    response = client.get("/analyze", params={"ticker": ticker})

    assert response.status_code == expected_status


def test_post_portfolio_returns_portfolio_summary(client):
    response = client.post(
        "/portfolio",
        json={"stocks": ["AAPL", "MSFT"]}
    )

    assert response.status_code == 200
    payload = response.json()
    assert set(payload["weights"]) == {"AAPL", "MSFT"}
    assert payload["stress_tests"][0]["Scenario"] == "Market Crash"


def test_post_portfolio_supports_maximum_allowed_portfolio_size(client):
    response = client.post(
        "/portfolio",
        json={"stocks": ["AAPL", "MSFT", "GOOG", "TSLA"]}
    )

    assert response.status_code == 200
    assert len(response.json()["weights"]) == 4


def test_post_portfolio_rejects_missing_stocks_field(client):
    response = client.post("/portfolio", json={})

    assert response.status_code == 422


@pytest.mark.parametrize(
    "payload",
    [
        {"stocks": []},
        {"stocks": [""]},
        {"stocks": ["AAPL", "MSFT", "GOOG", "TSLA", "NFLX"]},
        {"stocks": "AAPL"}
    ]
)
def test_post_portfolio_rejects_invalid_payloads(client, payload):
    response = client.post("/portfolio", json=payload)

    assert response.status_code in {400, 422}
