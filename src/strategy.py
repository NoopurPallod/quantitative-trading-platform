def generate_signals(data, short_window, long_window):
    data[f"MA{short_window}"] = data["Close"].rolling(window=short_window).mean()
    data[f"MA{long_window}"] = data["Close"].rolling(window=long_window).mean()
    data["Signal"] = 0
    data.loc[data[f"MA{short_window}"] > data[f"MA{long_window}"], "Signal"] = 1
    data["Position"] = data["Signal"].diff()
    return data