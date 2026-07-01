from flask import Flask, render_template, request
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']

    cleaned_news = preprocess_text(news)
    vector = vectorizer.transform([cleaned_news])

    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "🟢 Real News"
    else:
        result = "🔴 Fake News"

    return render_template('index.html', prediction=result, news=news)


if __name__ == "__main__":
    app.run(debug=True)
