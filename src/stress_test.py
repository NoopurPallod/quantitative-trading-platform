def stress_test(
    stocks,
    weights,
    stress_scenario,
    portfolio_value
):

    portfolio_loss_pct = 0

    for stock, weight in zip(
        stocks,
        weights
    ):

        portfolio_loss_pct += (
            weight *
            stress_scenario[stock]
        )

    stressed_value = (
        portfolio_value *
        (1 + portfolio_loss_pct)
    )

    loss = (
        portfolio_value -
        stressed_value
    )

    return (
        portfolio_loss_pct,
        stressed_value,
        loss
    )