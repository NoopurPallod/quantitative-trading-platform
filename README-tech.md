# Quant Trading Dashboard (Technical Overview)

A full-stack analytics platform built using React, FastAPI, and Python.

The application demonstrates end-to-end software engineering principles including frontend development, REST API design, backend analytics services, data processing pipelines, and interactive data visualization.

---

## Overview

The platform allows users to:

* Analyze historical stock data
* Execute strategy backtests
* Compare trading strategies
* Perform portfolio optimization
* Evaluate risk metrics
* Visualize financial analytics through an interactive web interface

The system is built using a modular architecture that separates data ingestion, analytics, API services, and frontend presentation layers.

---

## Technical Features

### Frontend

* React-based user interface
* Component-driven architecture
* State management using React Hooks
* API integration using Axios
* Interactive visualizations using Recharts
* Responsive dashboard layout

### Backend

* FastAPI REST API
* Modular analytics engine
* Portfolio optimization service
* Strategy evaluation service
* Risk analysis service
* JSON-based API responses

### Data Processing

* Historical market data ingestion
* Data cleaning and transformation
* Time-series return calculations
* Statistical analysis pipelines
* Risk metric computation

---

## System Architecture

```text
React Frontend
       │
       ▼
Axios API Requests
       │
       ▼
FastAPI Backend
       │
 ┌───────────────┬───────────────┬───────────────┐
 │               │               │
 ▼               ▼               ▼
Strategy      Portfolio       Risk
Engine        Engine          Engine
 │               │               │
 └───────────────┴───────────────┘
               │
               ▼
      Data Processing Layer
               │
               ▼
       Market Data Source
```

---

## Key Components

### Strategy Engine

Responsible for:

* Moving average generation
* Signal creation
* Strategy evaluation
* Performance comparison

### Backtesting Engine

Responsible for:

* Trade simulation
* Portfolio value tracking
* Historical performance measurement

### Portfolio Optimization Engine

Responsible for:

* Portfolio generation
* Monte Carlo simulation
* Allocation optimization
* Risk-adjusted performance analysis

### Risk Analytics Engine

Responsible for:

* Value-at-Risk computation
* Stress testing
* Volatility analysis

---

## Technology Stack

### Frontend

* React
* Axios
* Recharts
* CSS

### Backend

* FastAPI
* Python

### Data & Analytics

* Pandas
* NumPy
* yFinance

---

## Project Structure

```text
Trading-Platform/

├── frontend/
│   ├── src/
│   ├── App.jsx
│   └── App.css
│
├── backend/
│   └── main.py
│
├── src/
│   ├── analyze.py
│   ├── optimizer.py
│   ├── portfolio_optimizer.py
│   ├── strategy.py
│   ├── backtester.py
│   ├── metrics.py
│   ├── risk_metrics.py
│   ├── stress_test.py
│   └── data_loader.py
```

---

## Dashboard Screenshots

## Single Stock Strategy Analysis

![](assets/Single.png)

## Portfolio Optimization Dashboard

![](assets/Portfoilo.png)

## Risk Analytics Dashboard

![](assets/Risk.png)

---

## Installation

### Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Engineering Highlights

* Full-stack application architecture
* REST API development with FastAPI
* Data processing using Pandas and NumPy
* Monte Carlo simulation implementation
* Interactive financial data visualization
* Modular backend design
* Separation of concerns across services
* End-to-end analytics workflow

---

## Future Enhancements

* Authentication & User Accounts
* Database Integration
* Docker Deployment
* Cloud Hosting
* Real-Time Market Data
* Strategy Plug-in Framework
* Automated Report Generation

---

## Author

Developed by Noopur as a full-stack software engineering and analytics project.
