from flask import Flask, render_template, request
from sentiment_analysis import detect_sentiment  # your own function
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "ru": "Russian",
    "ja": "Japanese"
}

@app.route("/", methods=["GET", "POST"])
def index():
    original_text = ""
    translated_text = ""
    sentiment = ""
    target_lang = "fr"

    if request.method == "POST":
        original_text = request.form["text"]
        target_lang = request.form["target_lang"]

        try:
            sentiment = detect_sentiment(original_text)
        except Exception as e:
            sentiment = "Error"

        try:
            translated_text = GoogleTranslator(source='auto', target=target_lang).translate(original_text)
        except Exception as e:
            translated_text = f"Translation Error: {e}"

    return render_template("index.html",
                           original_text=original_text,
                           translated_text=translated_text,
                           sentiment=sentiment,
                           target_lang=target_lang,
                           languages=languages)



import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
