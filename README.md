# 🧢 Cap or No Cap – The Fitness Myth Buster

Cap or No Cap is a fun, interactive web app that busts fitness myths using machine learning. Just type in a myth you've heard, and the app will tell you if it’s "Cap" 🧢 or "No Cap" ✅ – backed by an ML model trained on over 300 myths!

🚀 **Live Demo:** [Click here to try it out](https://cap-or-nocap.onrender.com)

## ✨ Features
- Clean, minimalist UI with friendly fonts and color scheme
- Custom-trained ML model using TF-IDF + Logistic Regression
- Fully responsive and deployed using Render

## 🧠 Model Performance
- Achieved 77% accuracy on test data.
- Precision: 0.80 (Cap), 0.74 (No Cap)
- Recall: 0.75 (Cap), 0.80 (No Cap)
- F1-Score: ~0.77 across both classes

- **Label 0.0:** Cap (Myth)
- **Label 1.0:** No Cap (Truth)

## 🛠 Tech Stack
- **Frontend:** HTML, CSS (inline), JavaScript
- **Backend:** Flask (Python)
- **Model:** TF-IDF + Logistic Regression (sklearn)
- **Deployment:** Render
- **Version Control:** Git & GitHub

## 📂 How to Run Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/okayyananya/cap-or-no-cap.git
    cd cap-or-no-cap
    ```

2. Install dependencies:
    ```bash
    pip install flask scikit-learn joblib
    ```

3. Run the app:
    ```bash
    python app.py
    ```

4. Open in browser:
    ```
    http://localhost:5000
    ```

## 🙏 Credits
- Model training and app design by [Ananya Matta](https://www.linkedin.com/in/ananya-matta-47480a270/)

---

🧠 Bust myths, learn facts, and have fun with **Cap or No Cap**!

