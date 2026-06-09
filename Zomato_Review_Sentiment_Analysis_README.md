# Zomato Review Sentiment Analysis

An exploratory data science and natural language processing (NLP) workflow that analyzes customer reviews of Zomato restaurants. This project helps businesses understand customer feedback trends by classifying reviews into positive, negative, and neutral sentiments.

---

## Core Features

### Data Preprocessing
* Ingests CSV/JSON review datasets, handling missing values and duplicate rows.
* Standardizes review texts: Lowercasing, removing special characters, and converting emoticons.
* Implements stopword removal and lemmatization/stemming using the Natural Language Toolkit (NLTK).

### Sentiment Analysis
* Utilizes lexicon-based sentiment analysis (VADER) or supervised machine learning classifiers to determine polarity scores.
* Groups sentiment outcomes to analyze overall ratings and compare against customer-written reviews.

### Customer Review Analytics & Visualization
* Generates word clouds of positive and negative keywords.
* Visualizes review length distributions and rating distributions using Matplotlib and Seaborn.
* Identifies key trends in user feedback for individual restaurant hubs.

---

## Tech Stack
* Language: Python
* Libraries: Pandas, NumPy, NLTK, Matplotlib, Seaborn, WordCloud
* Environment: Jupyter Notebook

---

## Setup & Execution

### Prerequisites
* Python 3.8 or higher
* Jupyter Notebook

### Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/Zomato_Review_Sentiment_Analysis.git
   cd Zomato_Review_Sentiment_Analysis
   ```

2. Install python packages:
   ```bash
   pip install pandas numpy nltk matplotlib seaborn wordcloud
   ```

3. Download NLTK data:
   Open Python in your terminal and download required corpora:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('vader_lexicon')
   ```

4. Launch the notebook:
   ```bash
   jupyter notebook sentiment_analysis.ipynb
   ```

---

## License
Distributed under the MIT License. See `LICENSE` for details.
