# services/sentiment.py

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze sentiment of the input text and return label:
    'positive', 'neutral', or 'negative'
    
    Combines TextBlob polarity and VADER compound score.
    """
    if not text:
        return 'neutral'
    
    # TextBlob polarity: -1 to 1
    tb_polarity = TextBlob(text).sentiment.polarity
    
    # VADER compound: -1 to 1
    vader_score = analyzer.polarity_scores(text)['compound']
    
    # Simple average of both scores
    avg_score = (tb_polarity + vader_score) / 2
    
    if avg_score >= 0.05:
        return 'positive'
    elif avg_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'
