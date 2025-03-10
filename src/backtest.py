import pandas as pd

def backtest_strategy(df, predictions):
    """Simulate a simple trading strategy."""
    df['Signal'] = predictions
    df['Daily Return'] = df['Adj Close'].pct_change()
    
    # Strategy Return
    df['Strategy Return'] = df['Daily Return'] * df['Signal'].shift(1)
    cumulative_return = (1 + df['Strategy Return']).cumprod()

    return {
        "Total Return": cumulative_return.iloc[-1] - 1,
        "Average Daily Return": df['Strategy Return'].mean(),
        "Volatility": df['Strategy Return'].std()
    }
