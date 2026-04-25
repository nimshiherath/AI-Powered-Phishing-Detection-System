from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))



def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

SUSPICIOUS_WORDS = [
    "urgent", "verify", "password", "bank", "account",
    "click here", "confirm", "suspend", "login", "update",
    "credit card", "social security", "prize", "winner"   # expanded list
]

def check_keywords(text):
    lower = text.lower()
    return [w for w in SUSPICIOUS_WORDS if w in lower]   # returns which words, not just True/False

def contains_link(text):
    return bool(re.search(r'http|www\.', text))          #  more precise check



@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    reasons = []
    confidence = None

    if request.method == "POST":
        user_input = request.form.get("message", "").strip()

        if not user_input:                                 #  handle empty input
            return render_template("index.html", error="Please enter a message.")

        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])

        ai_pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]
        confidence = round(max(prob) * 100, 1)            #  confidence score

        matched_keywords = check_keywords(user_input)
        link_flag = contains_link(user_input)

        if ai_pred == 1 or matched_keywords or link_flag:
            result = "⚠️ Suspicious"
            if matched_keywords:
                reasons.append(f"Suspicious keywords: {', '.join(matched_keywords)}")
            if link_flag:
                reasons.append("Contains a link")
            if ai_pred == 1:
                reasons.append("AI model flagged this message")
        else:
            result = "✅ Safe"

    return render_template("index.html", result=result, reasons=reasons, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)