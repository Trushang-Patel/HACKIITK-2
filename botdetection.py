# -*- coding: utf-8 -*-
"""BotDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U1qE8FWBu7NYmoKxpop0bHqewn4BrnUz
"""

import pandas as pd
import numpy as np
import re
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from nltk.corpus import stopwords

# Load dataset
file_path = '/content/drive/MyDrive/IITHACK-IITROOPER/bot_detection_data.csv'
df = pd.read_csv(file_path)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

df['clean_text'] = df['Tweet'].apply(clean_text)

# TF-IDF Feature Extraction
vectorizer = TfidfVectorizer(max_features=5000)
X_text = vectorizer.fit_transform(df['clean_text'])

# Behavioral Features
df['engagement_ratio'] = df['Retweet Count'] / (df['Mention Count'] + 1)
df['log_followers'] = np.log1p(df['Follower Count'])

# Combine Features
X = np.hstack((X_text.toarray(), df[['engagement_ratio', 'log_followers']].values))
y = df['Bot Label']  # Target variable

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate Model
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Function to predict bot/human based on username
def predict_username(username):
    # Find user data based on username
    user_data = df[df['Username'] == username]
    if user_data.empty:
        return f"❌ Username '{username}' not found in the dataset."

    # Preprocess the user's tweet text
    clean_texts = vectorizer.transform(user_data['clean_text'])
    avg_tfidf = clean_texts.mean(axis=0).A.flatten()  # Sparse to dense array

    # Behavioral features for the user
    engagement_ratio = user_data['engagement_ratio'].values[0]
    log_followers = user_data['log_followers'].values[0]

    # Combine features
    features = np.hstack((avg_tfidf, [engagement_ratio, log_followers]))

    # Make the prediction
    prediction = clf.predict([features])[0]
    confidence = clf.predict_proba([features])[0][prediction]

    return f"🔍 Prediction for @{username}: {'🤖 Bot' if prediction == 1 else '👤 Human'} (Confidence: {confidence:.2f})"

# Example Usage
username_to_check = "pmason"  # Replace with any username from the dataset
result = predict_username(username_to_check)
print(result)