import pandas as pd

def moving_average(df, window):
    return df['Close'].rolling(window=window).mean()

def rsi(df, window=14):
    delta = df['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd(df, short_window=12, long_window=26, signal_window=9):
    short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal

def add_technical_indicators(df):
    """Add SMA, RSI, MACD to DataFrame."""
    df['SMA_50'] = moving_average(df, 50)
    df['SMA_200'] = moving_average(df, 200)
    df['RSI_14'] = rsi(df, 14)
    df['MACD'], df['Signal'] = macd(df)
    return df
