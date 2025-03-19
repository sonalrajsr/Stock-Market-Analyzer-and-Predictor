import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from src import data_loader

# Streamlit App Title
st.set_page_config(page_title="Algorithmic Trading Dashboard", layout="wide")
st.title("Algorithmic Trading Dashboard")

# Sidebar Inputs
st.sidebar.header("Stock Selection")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT)", "AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date(2023, 12, 31))

# Button to Fetch Data
if st.sidebar.button("Fetch Data"):
    try:
        data = data_loader.get_stock_data(ticker, start_date, end_date)
        st.success("✅ Data Fetched Successfully!")
        st.write(data)
        st.subheader("Stock Price Trends")
        fig, ax = plt.subplots(figsize=(12,6))
        ax.plot(data.Date, data["Close"], label="Stock Price", color='blue')
        ax.plot(data.Date, data["SMA_50"], label="50-day SMA", linestyle="dashed", color='red')
        ax.plot(data.Date, data["SMA_200"], label="200-day SMA", linestyle="dashed", color='green')
        ax.legend()
        st.pyplot(fig)

        # Plot Stock Prices
        st.subheader("Rleative Strength Index (RSI)")
        fig, ax = plt.subplots(figsize=(12,6))
        plt.plot(data.Date, data["RSI_14"], label="RSI (14)", color='purple')
        plt.axhline(70, linestyle="dashed", color="red", alpha=0.5, label="Overbought (70)")
        plt.axhline(30, linestyle="dashed", color="green", alpha=0.5, label="Oversold (30)")
        plt.title("Relative Strength Index (RSI)")
        plt.xlabel("Date")
        plt.ylabel("RSI Value")
        ax.legend()
        st.pyplot(fig)

        # Plot Stock macd
        st.subheader("Moving Average Convergence Divergence (MACD)")
        plt.figure(figsize=(12,6))
        plt.plot(data.Date, data["MACD"], label="MACD", color='black')
        plt.plot(data.Date, data["Signal"], label="Signal", linestyle="dashed", color='orange')
        plt.axhline(0, linestyle="dashed", color="gray", alpha=0.5)
        plt.title("MACD Indicator")
        plt.xlabel("Date")
        plt.ylabel("MACD Value")
        plt.legend()
        st.pyplot(plt)

        # Plot Stock Trading Volume
        plt.figure(figsize=(12,6))
        st.subheader("Stock Trading Volume")
        plt.bar(data.Date, data["Volume"], color="gray", alpha=0.7)
        plt.title("Stock Trading Volume Over Time")
        plt.xlabel("Date")
        plt.ylabel("Volume")
        st.pyplot(plt)
    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")
        st.stop()