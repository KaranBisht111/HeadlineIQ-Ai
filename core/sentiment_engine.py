# core/sentiment_engine.py

from textblob import TextBlob


class SentimentEngine:

    def detect_sentiment(self, text):

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0.2:
            return "positive"

        elif polarity < -0.2:
            return "negative"

        return "neutral"