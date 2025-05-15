# test_stock.py
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# from services.stocks import get_stock_info, get_stock_history

# ticker = "AAPL"

# info = get_stock_info(ticker)
# print("🟢 Current Info:")
# print(info)

# print("\n📈 Price History:")
# hist = get_stock_history(ticker)
# print(hist.tail())

from services import get_news_sentiment

if __name__ == "__main__":
    ticker = "AAPL"  # Or any stock you want
    news_items = get_news_sentiment(ticker)

    for article in news_items:
        print(f"[{article['sentiment'].upper()}] {article['title']}")
        print(f"URL: {article['url']}\n")
