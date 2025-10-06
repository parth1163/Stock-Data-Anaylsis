import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# -------------------------------
# Author: Parth Patel
# Purpose: Get stock data, calculate simple moving average (SMA),
# and show both on a graph.
# -------------------------------

TICKER = 'AAPL'       # Stock symbol (Apple Inc. by default)
DAYS_TO_LOOK_BACK = 90  # Last 90 days
SMA_PERIOD = 20         # 20-day SMA

def get_stock_data(ticker, days):
    """
    Gets recent stock data using yfinance.
    """
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')

    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            print("No data found. Check the ticker symbol.")
            return None
        return data
    except:
        print("Error while fetching data. Check connection or ticker.")
        return None

def calculate_sma(df, period):
    """
    Calculates simple moving average.
    """
    if df is not None:
        df[f'SMA_{period}'] = df['Close'].rolling(window=period).mean()
    return df

def plot_data(df, ticker, period):
    """
    Plots the close price and SMA on a line chart.
    """
    if df is not None:
        plt.figure(figsize=(12, 6))
        plt.plot(df['Close'], label='Close Price', color='blue')
        plt.plot(df[f'SMA_{period}'], label=f'{period}-Day SMA', color='red')
        plt.title(f'{ticker} Closing Price and {period}-Day SMA')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Main
if __name__ == "__main__":
    print(f"Getting data for {TICKER}...")

    stock_df = get_stock_data(TICKER, DAYS_TO_LOOK_BACK)

    if stock_df is not None:
        print("Data received. Calculating SMA...")

        stock_df = calculate_sma(stock_df, SMA_PERIOD)
        print("\nLast 5 rows of data:")
        print(stock_df[['Close', f'SMA_{SMA_PERIOD}']].tail())

        plot_data(stock_df, TICKER, SMA_PERIOD)
        print("\nChart displayed. Close the window to finish.")
    else:
        print("Failed to get stock data.")
