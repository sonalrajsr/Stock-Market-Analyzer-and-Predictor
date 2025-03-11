import yfinance as yf
from src.feature_engineering import rsi, macd
import numpy as np

def get_stock_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.columns = [col[0] for col in df.columns]
    df = df.reset_index()
    df.rename(columns={'index': 'Date'}, inplace=True)
    df['Return'] = df['Close'].pct_change()
    df['Target'] = np.where(df['Return'] > 0, 1, 0)  # (1 = up, 0 = down)

    # Technical Indicators
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    df['RSI_14'] = rsi(df, 14)
    df['MACD'], df['Signal'] = macd(df)
    return df.fillna(0)
