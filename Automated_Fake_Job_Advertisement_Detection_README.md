# Automated Fake Job Advertisement Detection

A machine learning-based fraud detection system designed to identify and classify fraudulent job postings. This project aims to protect job seekers from recruitment scams by filtering out untrustworthy advertisements.

---

## Core Features

### NLP Preprocessing Pipeline
* Text cleaning: Case normalization, removal of HTML tags, punctuation, and special characters.
* Tokenization and stopword removal to focus on high-significance terms.
* Vectorization: Converting textual data into numerical features using TF-IDF or Bag of Words representations.

### Classification Models
* Implements binary classification algorithms (such as Logistic Regression, Random Forest, or Naive Bayes) to distinguish between genuine and fake advertisements.
* Cross-validation to ensure model robustness and avoid overfitting.

### Evaluation Metrics
Detailed performance reporting using:
* Accuracy: Overall correctness of the model.
* Precision: The ratio of correctly identified fake ads to the total predicted fake ads.
* Recall (Sensitivity): The proportion of actual fake ads identified by the model.
* F1-Score: The harmonic mean of precision and recall.

---

## Tech Stack
* Language: Python
* Libraries: Pandas, NumPy, Scikit-Learn, NLTK
* Development Environment: Jupyter Notebook

---

## Installation & Usage

### Prerequisites
* Python 3.8 or higher
* Jupyter Notebook or JupyterLab

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/Automated_Fake_Job_Advertisement_Detection.git
   cd Automated_Fake_Job_Advertisement_Detection
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn nltk
   ```

3. Run the analysis:
   Open the Jupyter Notebook:
   ```bash
   jupyter notebook fake_job_detection.ipynb
   ```
   Execute the cells sequentially to preprocess the data, train the classifiers, and view performance metrics.

---

## License
Distributed under the MIT License. See `LICENSE` for more details.
