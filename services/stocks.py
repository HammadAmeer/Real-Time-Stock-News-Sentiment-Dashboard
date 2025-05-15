# services/stock.py

import yfinance as yf
import pandas as pd

def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "symbol": ticker.upper(),
            "shortName": info.get("shortName", "N/A"),
            "currentPrice": info.get("currentPrice"),
            "change": info.get("regularMarketChange"),
            "percentChange": info.get("regularMarketChangePercent"),
            "currency": info.get("currency")
        }
    except Exception as e:
        print("Error fetching stock info:", e)
        return {}

def get_stock_history(ticker: str, period='5d', interval='1h'):
    """
    Fetch historical price data for small graph.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        return hist
    except Exception as e:
        print(f"Error fetching stock history: {e}")
        return pd.DataFrame()
