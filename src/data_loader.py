import yfinance as yf

def get_stock_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.columns = [col[0] for col in df.columns]
    df = df.reset_index()  
    df.rename(columns={'index': 'Date'}, inplace=True)
    df['Return'] = df['Close'].pct_change()
    return df.dropna()
