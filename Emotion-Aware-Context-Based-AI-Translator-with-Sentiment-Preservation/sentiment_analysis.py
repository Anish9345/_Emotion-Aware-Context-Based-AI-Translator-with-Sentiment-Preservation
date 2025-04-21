from textblob import TextBlob

def detect_sentiment(text):
    """
    Detects sentiment from the given text (Positive, Neutral, Negative).
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"
