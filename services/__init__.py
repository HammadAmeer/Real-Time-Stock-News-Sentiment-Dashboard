# services/__init__.py

from .news import fetch_news
from .sentiment import analyze_sentiment

def get_news_sentiment(ticker, page_size=10):
    """
    Fetch recent news and return list of news with sentiment label.
    """
    news_list = fetch_news(ticker, page_size=page_size)
    for article in news_list:
        content = (article['title'] or '') + ' ' + (article['description'] or '')
        article['sentiment'] = analyze_sentiment(content)
    return news_list
