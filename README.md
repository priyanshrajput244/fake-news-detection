# 📰 Fake News Detection System

## Overview
The Fake News Detection System is a machine learning-based web application that classifies news articles as **Fake** or **Real**. The system analyzes the textual content of news articles using Natural Language Processing (NLP) techniques and a trained machine learning model to provide accurate predictions. This project aims to combat misinformation by helping users verify the authenticity of news content.

---

## Features
- Detects whether a news article is Fake or Real.
- Text preprocessing using NLP techniques.
- Machine Learning model for classification.
- User-friendly web interface.
- Fast and accurate predictions.
- Easy to deploy and extend.

---

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- NLTK

### Dataset
- Fake and Real News Dataset (Kaggle)

---

## Project Structure

```
Fake-News-Detection/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── Fake.csv
│   └── True.csv
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── model/
│   ├── train_model.py
│   └── preprocessing.py
│
└── screenshots/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detection.git
```

```bash
cd fake-news-detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Working

1. User enters a news article.
2. Text is preprocessed using NLP techniques.
3. Text is converted into numerical vectors using TF-IDF Vectorization.
4. The trained machine learning model predicts the result.
5. The application displays whether the news is **Fake** or **Real**.

---

## Machine Learning Pipeline

- Data Collection
- Data Cleaning
- Text Preprocessing
- Tokenization
- Stopword Removal
- Stemming/Lemmatization
- TF-IDF Vectorization
- Model Training
- Model Evaluation
- Prediction

---

## Algorithms

- Logistic Regression
- Passive Aggressive Classifier
- Naive Bayes
- Random Forest (Optional)

---

## Libraries Used

- Flask
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle

---

## Performance

| Metric | Score |
|---------|-------|
| Accuracy | 98% |
| Precision | 98% |
| Recall | 98% |
| F1-Score | 98% |

---

## Future Enhancements

- Deep Learning (LSTM/BERT)
- Real-time News Verification
- API Integration
- Multilingual News Detection
- Browser Extension
- Mobile Application
- Explainable AI Predictions

---

## Screenshots

Add screenshots of:
- Home Page
- Prediction Page
- Result Page
- Model Accuracy Graph

---

## Requirements

```
Flask
pandas
numpy
scikit-learn
nltk
joblib
```

---

## Authors

**Priyanshu**  
UID: **24BDA70343**

---

## License

This project is developed for educational and research purposes.
