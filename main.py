# main.py

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from services import get_news_sentiment
from services.stocks import get_stock_info, get_stock_history

# api_key = st.secrets["NEWSAPI_KEY"]

# --- Sidebar ---
st.sidebar.title("📊 Stock Sentiment Dashboard")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", "AAPL")
date_range = st.sidebar.slider("Select Date Range (days ago)", 1, 30, 7)

# --- Stock Info ---
st.title(f"📈 Stock Analysis for {ticker.upper()}")

stock_info = get_stock_info(ticker)
if stock_info:
    # st.write("DEBUG stock_info:", stock_info)
    # st.metric(label="Price", value=f"${stock_info['price']}", delta=f"{stock_info['change']} ({stock_info['percent_change']}%)")
    # st.metric(label="Price", value=f"${stock_info['price']}", delta=f"{stock_info['change']} ({stock_info['percent_change']}%)")
    if stock_info.get("currentPrice") is not None:
        st.metric(label="Price",value=f"${stock_info['currentPrice']}",
        delta=f"{stock_info['change']} ({stock_info['percentChange']}%)")
    else:
        st.warning("Stock data not available or invalid ticker.")
# --- Price Chart ---
st.subheader("Stock Price Chart")
history = get_stock_history(ticker)

if not history.empty:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=history.index, y=history['Close'], mode='lines', name='Close Price'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Price (USD)', height=400)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No price data available.")

# --- News and Sentiment ---
st.subheader("📰 Recent News & Sentiment")

news_items = get_news_sentiment(ticker, page_size=5)
sentiment_counts = {"positive": 0, "neutral": 0, "negative": 0}

for article in news_items:
    sentiment = article['sentiment']
    sentiment_counts[sentiment] += 1

    st.markdown(f"**[{article['title']}]({article['url']})**")
    st.write(article['description'])
    
    color = {
        "positive": "🟢 Positive",
        "neutral": "🟡 Neutral",
        "negative": "🔴 Negative"
    }
    st.markdown(f"**Sentiment:** {color[sentiment]}")
    st.markdown("---")

# --- Summary Chart ---
st.subheader("📊 Sentiment Summary")
st.write(sentiment_counts)
