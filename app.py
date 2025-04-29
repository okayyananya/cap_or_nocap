from flask import Flask, request, render_template
import joblib

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Load the model and vectorizer
model = joblib.load("cap_nocap_model.pkl")
vectorizer = joblib.load("cap_nocap_vectorizer.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)[0]
    label = "CAP" if prediction == 0 else "NO CAP"
    return render_template('index.html', prediction=label, user_text=text)

if __name__ == '__main__':
    app.run(debug=True)
