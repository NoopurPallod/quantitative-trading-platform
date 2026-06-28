from data_loader import load_data
from risk_metrics import calculate_var
from stress_test import stress_test
from validation import validate_stock_list

import pandas as pd
import numpy as np


SIMULATION_COUNT = 5000
RISK_FREE_RATE = 0.05
INITIAL_PORTFOLIO_VALUE = 100000


def calculate_portfolio_performance(returns, weights, risk_free_rate=RISK_FREE_RATE):
    portfolio_return = np.sum(
        returns.mean() * weights
    ) * 252

    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(
                returns.cov() * 252,
                weights
            )
        )
    )

    sharpe_ratio = (
        portfolio_return
        - risk_free_rate
    ) / portfolio_volatility

    return (
        float(portfolio_return),
        float(portfolio_volatility),
        float(sharpe_ratio)
    )


def optimize_portfolio(stocks):
    stocks = validate_stock_list(stocks)

    np.random.seed(42)

    prices = pd.DataFrame()

    for stock in stocks:

        data = load_data(
            stock,
            "2022-01-01",
            "2025-01-01"
        )

        prices[stock] = data["Close"]

    returns = prices.pct_change().dropna()

    portfolio_returns_list = []
    portfolio_volatility_list = []
    portfolio_sharpe_list = []
    weights_list = []

    for _ in range(SIMULATION_COUNT):

        weights = np.random.random(
            len(stocks)
        )

        weights = (
            weights
            / np.sum(weights)
        )

        (
            portfolio_return,
            portfolio_volatility,
            sharpe_ratio
        ) = calculate_portfolio_performance(
            returns,
            weights
        )

        portfolio_returns_list.append(
            portfolio_return
        )

        portfolio_volatility_list.append(
            portfolio_volatility
        )

        portfolio_sharpe_list.append(
            sharpe_ratio
        )

        weights_list.append(
            weights
        )

    best_index = np.argmax(
        portfolio_sharpe_list
    )

    best_weights = weights_list[
        best_index
    ]

    weights_dict = {}

    for stock, weight in zip(
        stocks,
        best_weights
    ):

        weights_dict[stock] = round(
            float(weight * 100),
            2
        )

    best_portfolio_returns = returns.dot(
        best_weights
    )

    var_95 = calculate_var(
        best_portfolio_returns
    )

    market_crash = {
        stock: -0.20
        for stock in stocks
    }

    severe_crash = {
        stock: -0.40
        for stock in stocks
    }

    random_stress = {}

    for stock in stocks:

        random_stress[stock] = -np.random.uniform(
            0.10,
            0.50
        )

    scenarios = {
        "Market Crash": market_crash,
        "Severe Crash": severe_crash,
        "Random Stress": random_stress
    }

    stress_results = []

    for (
        scenario_name,
        scenario
    ) in scenarios.items():

        (
            portfolio_loss_pct,
            stressed_value,
            loss
        ) = stress_test(
            stocks,
            best_weights,
            scenario,
            INITIAL_PORTFOLIO_VALUE
        )

        stress_results.append({

            "Scenario": scenario_name,

            "Loss %": round(
                float(
                    portfolio_loss_pct
                    * 100
                ),
                2
            ),

            "Portfolio Value": round(
                float(stressed_value),
                2
            ),

            "Loss Amount": round(
                float(loss),
                2
            )

        })

    return {

        "weights": weights_dict,

        "return": round(
            float(
                portfolio_returns_list[
                    best_index
                ] * 100
            ),
            2
        ),

        "volatility": round(
            float(
                portfolio_volatility_list[
                    best_index
                ] * 100
            ),
            2
        ),

        "sharpe": round(
            float(
                portfolio_sharpe_list[
                    best_index
                ]
            ),
            2
        ),

        "var": round(
            float(var_95 * 100),
            2
        ),

        "stress_tests":
        stress_results

    }
