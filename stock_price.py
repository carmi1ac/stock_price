import yfinance as yf

# Function to get stock information
def get_stock_price(ticker):
    # Download stock data
    stock = yf.Ticker(ticker)
    
    # Get the latest stock price
    stock_info = stock.history(period="1d")
    
    # Extract the latest closing price
    if not stock_info.empty:
        closing_price = stock_info['Close'].iloc[-1]
        print(f"The latest closing price of {ticker} is: ${closing_price:.2f}")
    else:
        print(f"No data found for ticker: {ticker}")

# Example usage
ticker_symbol = input("What stock would you like to check? (ticker): ")  # Replace with the desired stock ticker symbol

get_stock_price(ticker_symbol)
