# Quantitative Portfolio Analytics & Trading Strategy Platform

A quantitative finance platform designed to evaluate systematic trading strategies, construct risk-adjusted portfolios, and perform portfolio risk analysis using historical market data.

The platform combines strategy backtesting, portfolio optimization, Value-at-Risk estimation, and stress testing within an interactive analytics dashboard.

---

# Investment Research Workflow

The platform follows a quantitative investment workflow:

1. Retrieve historical market data
2. Generate trading signals
3. Backtest systematic strategies
4. Evaluate risk-adjusted performance
5. Construct optimized portfolios
6. Estimate downside risk
7. Perform stress testing under adverse market scenarios

---

# Quantitative Concepts Implemented

## Trading Strategy Backtesting

A Moving Average Crossover strategy is implemented to identify trend-following opportunities.

### Logic

Buy Signal:

```text
Short Moving Average > Long Moving Average
```

Sell Signal:

```text
Short Moving Average < Long Moving Average
```

The system evaluates multiple parameter combinations:

* MA20 / MA100
* MA20 / MA200
* MA50 / MA100
* MA50 / MA200

and ranks strategies using risk-adjusted performance metrics.

---

## Parameter Optimization

Multiple moving average combinations are tested using historical data.

Each strategy is evaluated based on:

* Portfolio Return
* Sharpe Ratio

The highest Sharpe Ratio strategy is selected as the optimal strategy.

---

## Portfolio Construction

The portfolio module allows multiple assets to be combined into a single portfolio.

Example assets:

* AAPL
* MSFT
* GOOG
* TSLA

Portfolio returns are calculated as:

```text
Portfolio Return
=
Weighted Sum of Asset Returns
```

Diversification effects are incorporated through covariance between asset returns.

---

## Monte Carlo Portfolio Optimization

The optimizer generates thousands of random portfolio allocations.

For each portfolio:

* Expected Annual Return is calculated
* Annual Volatility is calculated
* Sharpe Ratio is calculated

The optimal portfolio is defined as:

```text
Maximum Sharpe Ratio Portfolio
```

The process approximates the efficient frontier and identifies the allocation with the best risk-adjusted return profile.

---

## Efficient Frontier Simulation

The portfolio optimization engine generates 5,000 random portfolio allocations using Monte Carlo simulation.

For every simulated portfolio:

- Portfolio weights are randomly generated
- Expected Annual Return is calculated
- Annual Volatility is calculated
- Sharpe Ratio is calculated

Each portfolio is plotted in Risk-Return space:

- X-axis = Portfolio Volatility
- Y-axis = Expected Annual Return

This visualization approximates the Efficient Frontier and allows comparison of risk-adjusted portfolio performance.

The portfolio with the maximum Sharpe Ratio is identified as the optimal allocation and highlighted on the graph.

### Metrics Visualized

- Expected Return
- Portfolio Volatility
- Sharpe Ratio
- Optimal Portfolio Allocation

### Efficient Frontier Visualization

![Efficient Frontier](assets/graph.png)
## Risk Metrics

### Annual Return

Measures expected yearly portfolio growth.

Used to estimate long-term portfolio performance.

### Volatility

Measures dispersion of returns.

Higher volatility indicates greater uncertainty and risk.

### Sharpe Ratio

Measures excess return generated per unit of risk.

A higher Sharpe Ratio indicates superior risk-adjusted performance.

The optimization engine selects the portfolio with the highest Sharpe Ratio.

---

## Value at Risk (VaR)

The platform estimates Value-at-Risk using historical return distributions.

Purpose:

Estimate the potential loss that may occur over a given period under normal market conditions.

Example interpretation:

```text
95% VaR = -2.8%
```

indicates there is a 95% probability that losses will not exceed 2.8% during the specified period.

---

## Stress Testing Framework

The portfolio is evaluated under multiple adverse market scenarios.

### Market Crash Scenario

```text
All Assets = -20%
```

Purpose:

Simulate broad market corrections.

### Severe Crash Scenario

```text
All Assets = -40%
```

Purpose:

Simulate extreme systemic shocks.

### Random Stress Scenario

```text
Each Asset:
-10% to -50%
```

Purpose:

Simulate asymmetric sector-specific and company-specific shocks.

---

# Dashboard Features

## Single Stock Analytics

* Historical Price Analysis
* Moving Average Visualization
* Strategy Comparison
* Strategy Optimization
* Backtest Results

## Portfolio Analytics

* Portfolio Optimization
* Asset Allocation Analysis
* Return Forecasting
* Volatility Analysis
* Sharpe Ratio Analysis
* VaR Estimation
* Stress Testing

---

# Screenshots

## Single Stock Strategy Analysis

![](assets/Single.png)

## Portfolio Optimization Dashboard

![](assets/Portfoilo.png)

## Risk Analytics Dashboard

![](assets/Risk.png)


---

# Data & Methodology

### Market Data

Historical equity prices are retrieved using:

* Yahoo Finance (yFinance)

### Data Processing

* Pandas
* NumPy

### Portfolio Simulation

* 5,000 Monte Carlo Portfolios
* Risk-Free Rate Assumption
* Covariance Matrix Estimation
* Maximum Sharpe Optimization

---

# Practical Finance Concepts Demonstrated

This project demonstrates understanding of:

* Systematic Trading Strategies
* Trend Following
* Backtesting Methodology
* Portfolio Theory
* Diversification
* Risk-Adjusted Returns
* Sharpe Ratio Optimization
* Value-at-Risk (VaR)
* Stress Testing
* Monte Carlo Portfolio Simulation
* Efficient Frontier Analysis
* Maximum Sharpe Portfolio Selection
* Quantitative Portfolio Construction

---

# Future Extensions

* Efficient Frontier Visualization
* Sortino Ratio Optimization
* CAPM Analysis
* Fama-French Factor Models
* Black-Litterman Portfolio Construction
* Option Pricing Models
* Machine Learning-Based Alpha Signals
* Live Market Data Integration

---

# Author

Developed by Noopur as a quantitative finance, portfolio analytics, and risk management project.
