import yfinance as yf
import pandas as pd

def download_stock_data(stock_name, start_date, end_date):
    stock_data = yf.download(stock_name, start=start_date, end=end_date)
    stock_data.to_csv(f'{stock_name}.csv')

    data = pd.read_csv(f'{stock_name}.csv', skiprows=3)
    data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    return data


if __name__ == '__main__':
    stock_name = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    stock_data = download_stock_data(stock_name, start_date, end_date)
    print(stock_data)