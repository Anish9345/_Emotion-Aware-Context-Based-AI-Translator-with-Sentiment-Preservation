from flask import Flask, render_template, request
from googletrans import Translator
from sentiment_analysis import detect_sentiment  # Make sure this function works on English text

app = Flask(__name__)

# Language code dictionary for dropdown
LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'ru': 'Russian',
    'ja': 'Japanese',
    'de': 'German'
}

def translate_text(text, target_language):
    translator = Translator()
    try:
        detected_lang = translator.detect(text).lang

        # Translate to English for sentiment analysis if needed
        if detected_lang != 'en':
            temp_english_text = translator.translate(text, dest='en').text
            sentiment = detect_sentiment(temp_english_text)
        else:
            sentiment = detect_sentiment(text)

        # Final translation to target language
        translated_text = translator.translate(text, dest=target_language).text
        return sentiment, translated_text
    except Exception as e:
        return "Error", f"Translation Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        target_lang = request.form["target_lang"]
        sentiment, translated_text = translate_text(text, target_lang)
        return render_template("index.html", sentiment=sentiment, translated_text=translated_text, original_text=text, target_lang=target_lang, languages=LANGUAGES)
    
    return render_template("index.html", sentiment=None, translated_text=None, original_text="", target_lang="en", languages=LANGUAGES)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
