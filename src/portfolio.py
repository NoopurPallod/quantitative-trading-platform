from data_loader import load_data
import pandas as pd
import numpy as np
np.random.seed(42)
stocks = [
    "AAPL",  
    "JPM",  
    "XOM",    
    "JNJ",
    "TSLA"    
]

prices = pd.DataFrame()

for stock in stocks:

    data = load_data(
        stock,
        "2022-01-01",
        "2025-01-01"
    )

    prices[stock] = data["Close"]

print("\nClosing Prices\n")
print(prices.head())

returns = prices.pct_change().dropna()

print("\nDaily Returns\n")
print(returns.head())
weights = np.ones(len(stocks))
weights = weights / np.sum(weights)
portfolio_returns = returns.dot(weights)
print("\nPortfolio Returns\n")
print(portfolio_returns.head())
annual_return = portfolio_returns.mean() * 252
print(f"\nAnnual Return: {annual_return:.2%}")
annual_volatility = portfolio_returns.std() * (252 ** 0.5)
print(f"Annual Volatility: {annual_volatility:.2%}")
portfolio_returns_list = []
portfolio_volatility_list = []
portfolio_sharpe_list = []
weights_list = []

risk_free_rate = 0.05

for i in range(5000):

    weights = np.random.random(stocks.__len__())

    weights = weights / np.sum(weights)

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


print("\nBest Portfolio\n")

for stock, weight in zip(
    stocks,
    weights_list[best_index]
):
    print(
        f"{stock}: {weight:.2%}"
    )
print() 
print( f"Expected Return: " f"{portfolio_returns_list[best_index]:.2%}" ) 
print( f"Volatility: " f"{portfolio_volatility_list[best_index]:.2%}" ) 
print( f"Sharpe Ratio: " f"{portfolio_sharpe_list[best_index]:.2f}" ) 
print("\nMaximum Sharpe Ratio") 
print(max(portfolio_sharpe_list)) 
print("\nAverage Sharpe Ratio") 
print(np.mean(portfolio_sharpe_list))