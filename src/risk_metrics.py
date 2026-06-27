import numpy as np

def calculate_var(portfolio_returns, confidence_level=95):

    percentile = 100 - confidence_level

    var = np.percentile(
        portfolio_returns,
        percentile
    )

    return var