# Stock-Data-Anaylsis
A Python program that fetches recent stock data using yfinance, calculates a Simple Moving Average (SMA) with pandas, and visualizes both the closing price and SMA using matplotlib. Users can customize the stock ticker, date range, and SMA period to analyze short-term market trends.

The script uses:

yfinance → to get live stock data

pandas → to calculate the moving average

matplotlib → to plot the price and SMA

You can easily change the stock symbol, number of days to look back, and SMA period.

How It Works

Downloads recent stock data from Yahoo Finance

Calculates the SMA using pandas’ rolling mean

Displays a line chart showing the stock’s closing price (blue) and SMA (red)
