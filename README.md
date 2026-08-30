AI-Powered Phishing Detection

A web app that detects phishing emails using a machine learning model combined with rule-based heuristics. Users paste in email text and get an instant prediction of whether it's safe or suspicious, along with the reasons behind the decision.

How It Works

Text Cleaning – Input text is lowercased, and URLs, numbers, and punctuation are stripped out.
Feature Extraction – Cleaned text is converted into numerical features using TF-IDF (Term Frequency–Inverse Document Frequency).
ML Prediction – A Logistic Regression model, trained on a labeled phishing email dataset, predicts whether the message is phishing or legitimate, along with a confidence score.
Heuristic Checks – In addition to the model, the app independently checks for:
Suspicious keywords (e.g. "urgent", "verify", "password", "bank", "click here")
Presence of links (http or www.)
Combined Verdict – If the ML model flags it, or a suspicious keyword is found, or a link is present, the message is marked ⚠️ Suspicious. Otherwise, it's marked ✅ Safe. This layered approach helps catch phishing attempts even if the ML model alone misses them.
Tech Stack
Backend: Python, Flask
Machine Learning: scikit-learn (TF-IDF Vectorizer, Logistic Regression)
Data Handling: pandas
Frontend: HTML, CSS