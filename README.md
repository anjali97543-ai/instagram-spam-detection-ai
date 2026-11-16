# Instagram Spam Detection AI

🚀 **Live Demo:** [Click Here to Open Project](https://instagram-spam-detection-ai-9hg3faz7kawgu5fzujhl6g.streamlit.app/)


# 🛡️ Instagram Spam Detection AI

An AI-powered machine learning system designed to identify common spam and suspicious activity on social media platforms, with Instagram as the main case study.

## 📌 Overview

Social media platforms contain large amounts of spam, suspicious accounts, promotional comments, and potentially harmful links.

This project uses **Machine Learning, Natural Language Processing (NLP), and rule-based analysis** to help detect suspicious activity.

The system provides three main detection modules:

- 💬 Spam Comment Detection
- 👤 Fake/Suspicious Account Detection
- 🔗 Phishing Link Detection

## 🎯 Objectives

- Detect spam comments using NLP and Machine Learning.
- Identify potentially fake or suspicious accounts using account features.
- Detect common phishing indicators in URLs.
- Provide understandable reasons for why something was flagged.
- Create an easy-to-use web dashboard using Streamlit.

## 🧩 Modules

### 💬 1. Spam Comment Detection

Uses **NLP and Machine Learning** to classify Instagram comments as:

- ✅ Genuine Comment
- 🚨 Spam Comment

The system analyzes text patterns and spam-related indicators.

### 👤 2. Fake Account Detection

Analyzes account-related features such as:

- Followers
- Following
- Posts
- Likes
- Account age
- Profile picture
- Verification status
- Follower-following ratio
- Post frequency
- Login frequency
- Message frequency
- Activity score

The model predicts whether an account appears:

- ✅ Genuine
- ⚠️ Fake/Suspicious

### 🔗 3. Phishing Link Detection

Uses rule-based URL analysis to identify common phishing indicators.

The system checks factors such as:

- HTTPS usage
- IP-address-based URLs
- Unusually long URLs
- Suspicious keywords
- `@` symbols
- Excessive subdomains

The system provides:

- Risk level
- Phishing risk score
- Reasons for the detected risk

## 📊 Dataset

The project uses a dataset containing:

- **500 rows**
- **26 columns**
- **250 spam records**
- **250 non-spam records**
- **No missing values**

The dataset contains information related to both comments and account behavior.

## 🤖 Machine Learning

Two machine learning models are used:

1. **Spam Comment Detection Model**
2. **Fake Account Detection Model**

The models are trained and tested using a train-test split.

### Model Performance

| Model | Test Accuracy |
|---|---:|
| Spam Comment Detection | 100% |
| Fake Account Detection | 100% |

> ⚠️ The reported accuracy is based on this project's available test dataset. It should not be interpreted as guaranteed real-world accuracy.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF
- Joblib
- Streamlit
- Matplotlib

## 📂 Project Structure

```text
instagram-spam-detection-ai/
│
├── app.py
├── README.md
├── requirements.txt
│
├── spam_model.pkl
├── fake_model.pkl
├── vectorizer.pkl
│
├── train_spam.py
├── train_fake.py
├── phishing_detector.py
│
└── dataset/
    └── dataset.csv
