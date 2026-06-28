
# Quant Trading Dashboard (Technical Overview)
[![Python Tests](https://github.com/NoopurPallod/quantitative-trading-platform/actions/workflows/tests.yml/badge.svg)](https://github.com/NoopurPallod/quantitative-trading-platform/actions/workflows/tests.yml)

A full-stack analytics platform built with Python, FastAPI, React, Pandas, and NumPy that enables users to analyze historical stock data, backtest trading strategies, optimize portfolios, and visualize performance through an interactive dashboard.

---

## Features

### Full-Stack Architecture

* Built a React frontend and FastAPI backend connected through REST APIs.
* Implemented modular backend services for data processing, analytics, optimization, and visualization.
* Designed reusable frontend components and interactive dashboards.

### Stock Analytics Engine

* Processes historical market data using Pandas and NumPy.
* Generates trading signals using moving-average crossover strategies.
* Evaluates strategy performance across multiple parameter combinations.
* Computes returns, volatility, drawdowns, and performance metrics.

### Backtesting Framework

* Simulates trading strategies on historical market data.
* Tracks portfolio evolution over time.
* Computes daily returns and cumulative portfolio performance.
* Enables comparison between multiple strategy configurations.

### Portfolio Optimization

* Generates 5,000+ portfolio allocations using Monte Carlo simulation.
* Evaluates risk-return tradeoffs across asset combinations.
* Identifies optimal allocations based on configurable performance criteria.

### Risk Analysis

* Portfolio volatility measurement.
* Value-at-Risk (VaR) estimation.
* Scenario-based stress testing.
* Downside risk evaluation under adverse market conditions.

### Software Engineering Features

* RESTful API architecture using FastAPI.
* Automated testing using Pytest.
* Continuous Integration using GitHub Actions.
* Modular and maintainable codebase.
* Git-based development workflow.

---

## Tech Stack

### Languages

* Python
* JavaScript

### Backend

* FastAPI
* Pandas
* NumPy

### Frontend

* React
* Axios
* Recharts
* CSS

### Tooling

* Git
* GitHub
* GitHub Actions
* Pytest

---
## Development Workflow

* Source Control: Git & GitHub
* Continuous Integration: GitHub Actions
* Testing Framework: Pytest
* Automated validation on every push and pull request
---
## System Design

Frontend (React)

↓

REST API Layer (FastAPI)

↓

Analytics Services

├── Data Loading

├── Signal Generation

├── Backtesting

├── Portfolio Optimization

├── Risk Analysis

↓

Market Data Processing

(Pandas + NumPy)

---

## Key Engineering Highlights

* Developed a modular analytics pipeline separating data ingestion, strategy generation, optimization, and risk evaluation.
* Built REST APIs enabling seamless communication between frontend and backend services.
* Implemented numerical simulations and statistical computations using vectorized NumPy operations.
* Designed reusable React components for dashboards, charts, and portfolio visualizations.
* Added automated CI pipelines using GitHub Actions to validate code changes on every push and pull request.
* Implemented automated tests covering API endpoints, optimization modules, analytics workflows, and risk calculations.

---

## Test Coverage

Automated tests cover:

* API endpoints
* Portfolio optimization
* Strategy generation
* Risk metrics
* Stress testing
* End-to-end workflows

Current CI Status:

✅ GitHub Actions Passing

---

## Screenshots

### Dashboard Overview

## Single Stock Strategy Analysis

![](assets/Single.png)

## Portfolio Optimization Dashboard

![](assets/Portfoilo.png)

## Risk Analytics Dashboard

![](assets/Risk.png)

---

## Running Locally

### Backend

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend

```bash
npm install
npm run dev
```

---

## Future Enhancements

* Dockerized deployment
* User authentication
* Portfolio persistence with databases
* Real-time market data integration
* Advanced quantitative strategies
* Cloud deployment pipeline

---

## Learning Outcomes

This project provided hands-on experience with:

* Full-Stack Development
* REST API Design
* Python Backend Engineering
* React Frontend Development
* Data Processing Pipelines
* Automated Testing
* Continuous Integration (CI/CD)
* Software Architecture
* Git-Based Collaboration
* Numerical Computing with Pandas and NumPy
