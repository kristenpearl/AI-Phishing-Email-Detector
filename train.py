import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv("data/emails.csv")

X = data["email"]
y = data["label"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(X, y)

joblib.dump(model, "models/phishing_model.pkl")

print("Model trained successfully")
