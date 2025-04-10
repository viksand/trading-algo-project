# Example module to fetch market data

import yfinance as yf

def fetch_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data
# Test the function with a stock symbol (e.g., Apple)
if __name__ == "__main__":
    ticker = "AAPL"  # Apple Inc.
    start_date = "2020-01-01"
    end_date = "2021-01-01"
    data = fetch_data(ticker, start_date, end_date)
    print(data.head())  # Display the first 5 rows