# Intelligent Job Fraud Detection Platform

A multi-stage job verification and fraud detection system designed to protect job seekers from fake job advertisements and recruitment scams. The platform uses natural language processing (NLP) and machine learning to analyze job posts, while simultaneously performing verification checks on the job provider's digital and physical presence.

---

## Architecture Overview

The platform uses a hybrid architecture combining a Python machine learning core with a web-based dashboard:
* **Machine Learning & NLP Core (Python)**: Handles text analysis, feature extraction, web scraping, and domain authentication checks.
* **Dashboard & Portal Interface (JavaScript)**: Manages candidate inputs, displays verification reports, and presents explainable risk scores.

---

## Core Features

### 1. Fake Job Detection (NLP & Machine Learning)
* Preprocesses natural language job descriptions using spaCy (tokenization, lemmatization, stopword removal).
* Converts text features into numerical vectors using Term Frequency-Inverse Document Frequency (TF-IDF).
* Classifies advertisements using a Random Forest ensemble model to detect fraudulent patterns.

### 2. Multi-Stage Recruiter Verification
Unlike standard text classifiers, this platform executes secondary validations on the job provider:
* **Email & Domain Audit**: Validates email formats and queries domain authenticity using WHOIS records to check registration dates and domain age.
* **Company Legitimacy Checks**: Cross-references company websites, checks for active SSL certificates, and reviews online presence.
* **Location Audits**: Matches declared office locations against mapping and location intelligence resources.

### 3. Explainable Risk Scoring
* Generates a numerical fraud risk score.
* Produces a final verdict categorization: `Likely Genuine`, `Suspicious`, or `High Scam Risk`.
* Outlines the specific indicators (e.g., mismatched domain, high-risk text features) that triggered the verdict.

### 4. Automated Job Verification Reports
* Compiles text analysis and domain verification results into a single, clean report for job seekers.
* Structures raw unstructured job posting texts into standardized fields (Title, Company, Salary, Requirements).

### 5. Future Roadmap
* Integration with India's MCA21 (Ministry of Corporate Affairs) database for automated company registration verification.
* Development of crowdsourced scam intelligence feeds to flag recurring scam patterns in real-time.

---

## Tech Stack

* **Machine Learning & NLP (Python)**: Scikit-Learn, spaCy, Pandas, NumPy, TF-IDF, Random Forest
* **Web Scraping & APIs**: BeautifulSoup, Requests, WHOIS API, Web scraping APIs
* **Web Interface & Server**: JavaScript, Node.js, HTML5, CSS3
* **Environments**: Google Colab (Model calibration), Local IDE

---

## Installation & Setup

### Prerequisites
* Python 3.9 or higher
* Node.js (v18 or higher)
* Active WHOIS API credential

### Model & Scraper Backend Setup (Python)
1. Navigate to the core directory:
   ```bash
   cd core
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn spacy beautifulsoup4 requests python-dotenv
   python -m spacy download en_core_web_sm
   ```

### Web Portal Setup (Node.js/JavaScript)
1. Navigate to the root directory:
   ```bash
   npm install
   ```
2. Start the development portal:
   ```bash
   npm start
   ```

---

## License
Distributed under the MIT License. See `LICENSE` for details.
