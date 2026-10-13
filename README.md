# 🛡️ AI-Powered Phishing Detection System

An intelligent web application that detects phishing emails and malicious messages by combining **Machine Learning (NLP)** with **rule-based heuristics**. 

Users can paste email or message content into the web interface and receive an instant classification (**⚠️ Suspicious** or **✅ Safe**), accompanied by a confidence percentage and an explainable breakdown of why the message was flagged.

---

## 📌 Project Overview & Purpose

Cybercriminals frequently craft phishing emails using social engineering tactics—such as fake urgency, account suspension warnings, and credential harvesting prompts. While traditional filters look only for known malicious links, attackers continually adapt.

This project uses a **hybrid / layered detection strategy**:
1. **Machine Learning Model (Semantics & Tone):** A TF-IDF vectorizer + Logistic Regression classifier trained on thousands of labeled emails to identify deceptive language patterns.
2. **Rule-Based Heuristic Engine (High-Risk Triggers):** Independent pattern scanners that check for active links (`http`, `www.`) and urgent/financial trigger keywords (e.g., *"urgent"*, *"verify"*, *"bank"*, *"password"*).
3. **Explainability Layer:** Clearly reports why an email was flagged (e.g., matched keywords, links present, or ML classification) rather than acting as a black box.

---

## 🚀 Key Features

- **Hybrid Detection Engine:** Minimizes false negatives by combining ML probability with deterministic keyword and URL rules.
- **Explainable Verdicts:** Outlines specific reasons behind every alert (e.g., *Suspicious keywords: verify, account*, *Contains a link*).
- **Confidence Scoring:** Displays the model's prediction probability percentage.
- **Fast & Lightweight:** Built using Flask and Scikit-Learn with minimal overhead and instantaneous response times.
- **Clean UI:** Responsive web interface with real-time feedback and input validation.

---

## 🧠 How It Works

```
   Raw Email Text
         │
         ├───► [ 1. Heuristic Scanner ] ───► Check for URLs & Suspicious Keywords
         │
         └───► [ 2. Text Preprocessing ] ──► Lowercase, remove URLs, numbers, & punctuation
                     │
                     ▼
               [ 3. TF-IDF Vectorizer ] ──► Convert text to 5,000 top n-gram features
                     │
                     ▼
               [ 4. Logistic Regression ] ► Compute Phishing Probability & Prediction
                     │
                     ▼
   [ Combined Decision Logic ]
   Flagged if: ML Model flags Phishing  OR  Link is found  OR  Keywords matched
         │
         ▼
   Final Verdict (⚠️ Suspicious / ✅ Safe) + Confidence + Explanations
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Web Framework:** [Flask](https://flask.palletsprojects.com/)
- **Machine Learning & NLP:** [scikit-learn](https://scikit-learn.org/) (`TfidfVectorizer`, `LogisticRegression`)
- **Data Handling:** [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Frontend:** HTML5, CSS3 (Jinja2 templates)

---

## 📁 Project Structure

```text
AI-Powered-Phishing-Detection-System/
├── app.py                  # Flask web server and real-time detection logic
├── train.py                # Model training, evaluation, and serialization script
├── model.pkl               # Trained Logistic Regression model (serialized)
├── vectorizer.pkl          # Trained TF-IDF vectorizer (serialized)
├── phishing_email.csv      # Labeled dataset used for training
├── requirements.txt        # Project dependencies
├── templates/
│   └── index.html          # Web interface template
└── static/
    └── style.css           # Styling and layout
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/nimshiherath/AI-Powered-Phishing-Detection-System.git
cd AI-Powered-Phishing-Detection-System
```

### 3. Create and Activate a Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. Paste any email content into the text box and click **Check** to test.

---

## 🔄 Retraining the Model (Optional)

If you have an updated `phishing_email.csv` dataset, you can retrain the model and regenerate `model.pkl` and `vectorizer.pkl`:

```bash
python train.py
```

This will:
1. Clean and tokenize text from the dataset.
2. Fit a `TfidfVectorizer` (up to 5,000 features).
3. Train a `LogisticRegression` classifier with an 80/20 train-test split.
4. Output accuracy metrics and classification reports to the console.
5. Export updated `model.pkl` and `vectorizer.pkl` files.

---

## 🔍 Monitored Keywords & Heuristics

The rule-based layer specifically looks for high-frequency social engineering keywords:
- `urgent`, `verify`, `password`, `bank`, `account`
- `click here`, `confirm`, `suspend`, `login`, `update`
- `credit card`, `social security`, `prize`, `winner`

Any inclusion of hyperlinking patterns (`http` or `www.`) is also flagged automatically.

---

## 📜 Disclaimer
This project is intended for educational and defensive cybersecurity awareness purposes. It should be used as an auxiliary screening tool alongside standard email security protocols (SPF/DKIM/DMARC) and secure email gateways.