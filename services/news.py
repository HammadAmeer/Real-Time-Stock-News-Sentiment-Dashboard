# services/news.py

from newsapi import NewsApiClient
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)

def fetch_news(ticker, page_size=10):
    """
    Fetch latest news articles mentioning the stock ticker symbol.
    """
    query = f'"{ticker}" OR "{ticker} stock"'
    from_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
    all_articles = newsapi.get_everything(
        q=query,
        language='en',
        from_param=from_date,
        sort_by='publishedAt',
        page_size=page_size
    )
    
    articles = []
    for article in all_articles.get('articles', []):
        articles.append({
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'url': article.get('url', '')
        })
    return articles
