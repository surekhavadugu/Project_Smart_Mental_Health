from textblob import TextBlob

def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"