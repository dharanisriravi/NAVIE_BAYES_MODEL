
# train_model.py
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv('manual_data.csv')

# Prepare data
X = df['text']
y = df['language']

# Create pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train model
model.fit(X, y)

# Save model
with open('lang_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Language Detection Model trained and saved!")
