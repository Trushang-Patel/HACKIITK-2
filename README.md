# Social Media Bot Detection

This project aims to build an automated bot detection system for social media platforms. The goal is to detect and classify bot accounts based on their content patterns, posting behaviors, and engagement metrics. The system leverages machine learning and natural language processing techniques to identify bots and provide insights into suspicious activities.

## Objectives
1. **Bot Detection Mechanism:**
   - Detect bots using content features like sentiment, linguistic patterns, and textual analysis.
   - Identify anomalies in user behavior, such as high-frequency posts, repetitive content, and unnatural engagement.
   - Provide a confidence score indicating the likelihood of an account being a bot.

2. **Scalability and Performance:**
   - Ensure the system can efficiently handle large-scale data, with real-time processing capabilities.
   - Implement scalable data pipelines to process millions of social media posts.

3. **Detection Reports and Insights:**
   - Generate structured output to summarize detection results.
   - Provide insights into bot behavior and trends across social media platforms.

## Features
- **Text-based Feature Extraction:** Using TF-IDF, sentiment analysis, and word embeddings (Word2Vec, BERT).
- **Behavioral Feature Extraction:** Track user activity patterns, hashtag usage, and post timing.
- **Engagement Metrics:** Measure likes, shares, comments, and user mentions to detect automation.
- **Anomaly Detection Models:** Implement Isolation Forest and Autoencoders to identify abnormal behavior.
- **Time-series Analysis:** Use LSTMs to track account activity over time.
- **Scalability:** Leverage Apache Spark/Dask for distributed processing to handle large datasets.
- **Privacy:** Anonymization of personally identifiable information (PII) and secure data storage.

## Installation

### Prerequisites:
- Python 3.8 or higher

1. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download the required dataset (e.g., Twitter Bot Detection Dataset).  
   Unzip the dataset and place it in the `data/` directory.
   
### Setup:
1. Clone this repository:
   ```bash
   git clone https://github.com/Trushang-Patel/HACKIITK-2.git
   cd HACKIITK-2

## Evaluation Metrics

- **Precision:** Proportion of true positives among predicted bot accounts.
- **Recall:** Proportion of true positives identified among all actual bot accounts.
- **F1 Score:** Harmonic mean of precision and recall.
- **AUC-ROC:** Area Under the Curve (AUC) of the Receiver Operating Characteristic (ROC) curve.

## Demo Video

A demo showcasing the bot detection system and its functionality is available.

Click here to watch the vedio:
https://drive.google.com/file/d/1MJey9QfCXCS06UuNklBpDK5EAHssjcg0/view?usp=sharing
