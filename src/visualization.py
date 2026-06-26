import matplotlib.pyplot as plt

def plot_portfolio(data):

    plt.figure(figsize=(14, 7))

    plt.plot(
        data.index,
        data["Portfolio Value"],
        label="Portfolio Value"
    )

    plt.title("Portfolio Growth")

    plt.xlabel("Date")

    plt.ylabel("Portfolio Value")

    plt.legend()

    plt.show()