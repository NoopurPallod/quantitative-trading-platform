import { useState } from "react";
import axios from "axios";
import "./App.css";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Legend,
  CartesianGrid,
  PieChart,
  Pie,
  Cell
} from "recharts";

const STOCK_OPTIONS = ["AAPL", "MSFT", "GOOG", "TSLA"];
const PIE_COLORS = ["#3b82f6", "#22c55e", "#a855f7", "#f97316", "#06b6d4"];

function formatPercent(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) {
    return "--";
  }

  return `${Number(value).toFixed(2)}%`;
}

function formatNumber(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) {
    return "--";
  }

  return Number(value).toFixed(2);
}

function formatCurrency(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) {
    return "--";
  }

  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 2
  }).format(Number(value));
}

function App() {
  const [page, setPage] = useState("stock");
  const [stock, setStock] = useState("AAPL");
  const [result, setResult] = useState(null);
  const [portfolioStocks, setPortfolioStocks] = useState(["AAPL", "MSFT"]);
  const [portfolioResult, setPortfolioResult] = useState(null);

  async function runAnalysis() {
    const response = await axios.get(
      `https://quantitative-trading-platform.onrender.com/analyze?ticker=${stock}`
    );

    setResult(response.data);
  }

  function toggleStock(ticker) {
    if (portfolioStocks.includes(ticker)) {
      if (portfolioStocks.length === 1) {
        return;
      }

      setPortfolioStocks(
        portfolioStocks.filter((currentStock) => currentStock !== ticker)
      );

      return;
    }

    setPortfolioStocks([...portfolioStocks, ticker]);
  }

  async function optimizePortfolio() {
    const response = await axios.post(
      "https://quantitative-trading-platform.onrender.com/portfolio",
      {
        stocks: portfolioStocks
      }
    );

    setPortfolioResult(response.data);
  }

  const allocationData = portfolioResult
    ? Object.entries(portfolioResult.weights).map(([ticker, weight]) => ({
        name: ticker,
        value: Number(weight)
      }))
    : [];

  return (
    <div className="container">
      <header className="hero">
        <h1 className="title">Quant Trading Dashboard</h1>
        <p className="hero-subtitle">
          Explore individual stock signals and compare portfolio scenarios in a
          cleaner, faster interface.
        </p>
      </header>

      <div className="navbar">
        <button
          className={page === "stock" ? "nav-btn active" : "nav-btn"}
          onClick={() => setPage("stock")}
        >
          Single Stock
        </button>

        <button
          className={page === "portfolio" ? "nav-btn active" : "nav-btn"}
          onClick={() => setPage("portfolio")}
        >
          Portfolio Optimization
        </button>
      </div>

      {page === "stock" && (
        <>
          <div className="controls card card-soft">
            <div className="section-heading left-align">
              <h2>Single Stock Analysis</h2>
              <p>Choose a ticker and run the strategy comparison.</p>
            </div>

            <div className="control-row">
              <select value={stock} onChange={(e) => setStock(e.target.value)}>
                {STOCK_OPTIONS.map((ticker) => (
                  <option key={ticker}>{ticker}</option>
                ))}
              </select>

              <button className="analyze-btn" onClick={runAnalysis}>
                Run Analysis
              </button>
            </div>
          </div>

          {result && (
            <div className="card">
              <div className="section-heading">
                <h2>Best Strategy</h2>
                <p>Top-performing moving average combination for {stock}.</p>
              </div>

              <div className="metrics-grid">
                <div className="stat-card accent-blue">
                  <span>Strategy</span>
                  <strong>
                    MA{result.best_strategy["Short MA"]}/
                    MA{result.best_strategy["Long MA"]}
                  </strong>
                </div>

                <div className="stat-card accent-green">
                  <span>Return</span>
                  <strong>{formatPercent(result.best_strategy["Return"])} </strong>
                </div>

                <div className="stat-card accent-purple">
                  <span>Sharpe Ratio</span>
                  <strong>{formatNumber(result.best_strategy["Sharpe"])} </strong>
                </div>
              </div>
            </div>
          )}

          {result && result.chart_data && (
            <div className="card">
              <div className="section-heading left-align">
                <h2>Price vs Moving Averages</h2>
                <p>Trend view across price, short MA, and long MA.</p>
              </div>

              <div className="chart-container">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={result.chart_data}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                    <XAxis dataKey="date" stroke="#94a3b8" />
                    <YAxis stroke="#94a3b8" />
                    <Tooltip />
                    <Legend />
                    <Line
                      type="monotone"
                      dataKey="close"
                      name="Price"
                      stroke="#60a5fa"
                      strokeWidth={2.5}
                      dot={false}
                    />
                    <Line
                      type="monotone"
                      dataKey="ma_short"
                      name="Short MA"
                      stroke="#34d399"
                      strokeWidth={2.2}
                      dot={false}
                    />
                    <Line
                      type="monotone"
                      dataKey="ma_long"
                      name="Long MA"
                      stroke="#f87171"
                      strokeWidth={2.2}
                      dot={false}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </div>
          )}

          {result && (
            <div className="card">
              <div className="section-heading left-align">
                <h2>All Strategies</h2>
                <p>Compare every moving average pair returned by the backend.</p>
              </div>

              <div className="table-shell">
                <table>
                  <thead>
                    <tr>
                      <th>Strategy</th>
                      <th>Return</th>
                      <th>Sharpe</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.all_strategies.map((strategy, index) => (
                      <tr key={index}>
                        <td>
                          MA{strategy["Short MA"]}/MA{strategy["Long MA"]}
                        </td>
                        <td>{formatPercent(strategy["Return"])} </td>
                        <td>{formatNumber(strategy["Sharpe"])} </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </>
      )}

      {page === "portfolio" && (
        <div className="card portfolio-card">
          <div className="section-heading">
            <h2>Portfolio Optimization</h2>
            <p>
              Select your basket using ticker pills, then review weights, risk,
              and stress scenarios in a cleaner dashboard.
            </p>
          </div>

          <div className="selection-panel">
            <div className="selection-header">
              <div>
                <h3>Choose Stocks</h3>
                <p>Selected: {portfolioStocks.join(", ")}</p>
              </div>
              <button className="analyze-btn" onClick={optimizePortfolio}>
                Optimize Portfolio
              </button>
            </div>

            <div className="ticker-tabs" role="tablist" aria-label="Select stocks">
              {STOCK_OPTIONS.map((ticker) => {
                const isActive = portfolioStocks.includes(ticker);

                return (
                  <button
                    key={ticker}
                    type="button"
                    className={isActive ? "ticker-pill active" : "ticker-pill"}
                    onClick={() => toggleStock(ticker)}
                    aria-pressed={isActive}
                  >
                    <span className="ticker-symbol">{ticker}</span>
                    <span className="ticker-state">
                      {isActive ? "Selected" : "Tap to add"}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          {portfolioResult && (
            <div className="portfolio-results">
              <div className="metrics-grid compact-metrics">
                <div className="stat-card accent-green">
                  <span>Expected Return</span>
                  <strong>{formatPercent(portfolioResult.return)}</strong>
                </div>

                <div className="stat-card accent-blue">
                  <span>Volatility</span>
                  <strong>{formatPercent(portfolioResult.volatility)}</strong>
                </div>

                <div className="stat-card accent-purple">
                  <span>Sharpe Ratio</span>
                  <strong>{formatNumber(portfolioResult.sharpe)}</strong>
                </div>

                <div className="stat-card accent-orange">
                  <span>VaR</span>
                  <strong>{formatPercent(portfolioResult.var)}</strong>
                </div>
              </div>

              <div className="results-layout">
                <div className="card inner-card">
                  <div className="section-heading left-align compact-heading">
                    <h2>Portfolio Allocation</h2>
                    <p>Recommended portfolio mix across selected tickers.</p>
                  </div>

                  <div className="allocation-chart-wrap">
                    <div className="allocation-pie">
                      <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                          <Pie
                            data={allocationData}
                            dataKey="value"
                            nameKey="name"
                            innerRadius={68}
                            outerRadius={102}
                            paddingAngle={3}
                            stroke="rgba(15, 23, 42, 0.9)"
                            strokeWidth={4}
                          >
                            {allocationData.map((entry, index) => (
                              <Cell
                                key={entry.name}
                                fill={PIE_COLORS[index % PIE_COLORS.length]}
                              />
                            ))}
                          </Pie>
                          <Tooltip
                            formatter={(value) => formatPercent(value)}
                            contentStyle={{
                              backgroundColor: "#0f172a",
                              border: "1px solid rgba(71, 85, 105, 0.5)",
                              borderRadius: "12px"
                            }}
                          />
                        </PieChart>
                      </ResponsiveContainer>
                    </div>

                    <div className="allocation-legend">
                      {allocationData.map((entry, index) => (
                        <div key={entry.name} className="allocation-legend-item">
                          <div className="allocation-legend-label">
                            <span
                              className="allocation-dot"
                              style={{
                                backgroundColor:
                                  PIE_COLORS[index % PIE_COLORS.length]
                              }}
                            />
                            <span className="allocation-legend-ticker">
                              {entry.name}
                            </span>
                          </div>
                          <strong>{formatPercent(entry.value)}</strong>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="card inner-card">
                  <div className="section-heading left-align compact-heading">
                    <h2>Stress Testing</h2>
                    <p>How the portfolio behaves under downside scenarios.</p>
                  </div>

                  <div className="table-shell">
                    <table>
                      <thead>
                        <tr>
                          <th>Scenario</th>
                          <th>Loss %</th>
                          <th>Portfolio Value</th>
                          <th>Loss Amount</th>
                        </tr>
                      </thead>
                      <tbody>
                        {portfolioResult.stress_tests.map((test, index) => (
                          <tr key={index}>
                            <td>{test["Scenario"]}</td>
                            <td>{formatPercent(test["Loss %"])} </td>
                            <td>{formatCurrency(test["Portfolio Value"])} </td>
                            <td>{formatCurrency(test["Loss Amount"])} </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
