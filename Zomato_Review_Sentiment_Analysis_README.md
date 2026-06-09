# Zomato Review Sentiment Analysis

An exploratory data science and natural language processing (NLP) workflow designed to examine customer sentiment in restaurant reviews. This project structures and visualizes raw customer feedback, classifying it into positive, negative, and neutral scores to assist restaurant managers in optimizing customer service.

---

## Core Features

### Data Cleaning & Preprocessing
* Sanitizes unstructured text reviews: Handling missing values, removing special characters, and converting text to lowercase.
* Natural Language Processing: Stopword removal, tokenization, and word normalization using lemmatization via the NLTK library.

### Sentiment Analysis Models
* Lexicon-based sentiment scoring using VADER (Valence Aware Dictionary and Sentiment Reasoner) for rapid polarity classification.
* Supervised sentiment classification pipelines using traditional machine learning algorithms.

### Analytics & Visualizations
* Generates rating distributions and review length comparisons.
* Produces word frequency tables and word clouds highlighting positive and negative sentiment keywords.
* Visualizations implemented using Matplotlib and Seaborn.

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

2. Install dependencies:
   ```bash
   pip install pandas numpy nltk matplotlib seaborn wordcloud
   ```

3. Download NLP corpora:
   Open Python in your shell and execute:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('vader_lexicon')
   ```

4. Open the Jupyter interface:
   ```bash
   jupyter notebook sentiment_analysis.ipynb
   ```

---

## License
Distributed under the MIT License. See `LICENSE` for details.
