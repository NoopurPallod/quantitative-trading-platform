import yfinance as yf
import matplotlib.pyplot as plt
data = yf.download(
    "AAPL",
    start="2022-01-01",
    end="2025-01-01"
)
data.columns = data.columns.get_level_values(0)
data["MA50"] = data["Close"].rolling(window=50).mean()
data["MA200"] = data["Close"].rolling(window=200).mean()
plt.figure(figsize=(14,7))

plt.plot(
    data.index,
    data["Close"],
    label="Close Price"
)

plt.plot(
    data.index,
    data["MA50"],
    label="50-Day MA"
)

plt.plot(
    data.index,
    data["MA200"],
    label="200-Day MA"
)

plt.title("Moving Average Strategy")

plt.xlabel("Date")

plt.ylabel("Price")

plt.legend()

data["Signal"] = 0
data.loc[data["MA50"] > data["MA200"],"Signal"] = 1
data["Position"] = data["Signal"].diff()
data["Action"] = "Hold"
data.loc[data["Position"] == 1, "Action"] = "Buy"
data.loc[data["Position"] == -1, "Action"] = "Sell"
print(data[["Close", "MA50", "MA200", "Signal", "Action"]].tail(40))
plt.show()