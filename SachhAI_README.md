# SachhAI — Interview Authenticity Platform

SachhAI is an interview authenticity detection system designed for HR teams and technical recruiters. It detects whether a candidate's technical interview responses are genuinely their own or externally assisted (AI-generated or pre-written) during live calls.

The system establishes a natural communication baseline by collecting a casual personal response, compares it against a formal technical response, and runs analysis across 11 distinct style dimensions.

---

## Core System Architecture

```
chrome-extension / meet-extension (Google Meet / Web Injection)
                     ↓ HTTP REST / WebSockets
backend/server.py (FastAPI, port 8000)
         ├── /voice/*       ← style comparator, Deepgram transcriber, Winston AI API
         ├── /auth/*        ← JWT login & registration
         └── /calibrate/*   ← calibration & testing endpoints
```

---

## Technical Features

### 1. Browser Extensions
* **Chrome Extension**: Injects interview recording and tracking controls directly into major web-based interview environments.
* **Google Meet Extension**: Captures active WebRTC audio streams from the tab, feeds them into the transcription pipeline, and shows live alerts.

### 2. Style Shift Analysis (The 11 Parameters)
The core analysis engine runs a style shift comparator across 11 key dimensions to detect discrepancies:

| Parameter | Weight | Description |
| --- | --- | --- |
| vocabulary_level | 2.5 | Syllable-weighted word complexity metric (0-100) |
| flesch_kincaid | 2.2 | Grade Level — higher index indicates complex text |
| formality_score | 2.0 | Composite score based on sentence lengths and filler density |
| gunning_fog | 1.8 | Fog index penalizing excessive multi-syllable terms |
| hedging_density | 1.8 | Frequency of epistemic hedges ("it is worth noting", etc.) |
| passive_voice_ratio | 1.5 | Frequency of passive voice structures |
| grammar_score | 1.2 | Penalizes formatting and structural disfluencies |
| avg_sentence_len | 1.2 | Average word count per sentence |
| filler_ratio | 0.8 | Frequency of filler words ("um", "like", "you know") |
| transition_density | 2.0 | Frequency of formal transitional adverbs ("furthermore", etc.) |
| sentence_burstiness | 2.0 | Coefficient of variation in sentence length |

### 3. Machine Learning Classification Model
* **Model Type**: Scikit-Learn Pipeline (standard scaler + RandomForest/GradientBoosting classifier).
* **Feature Engineering**: 29 features comprising 15 style delta scores, 9 raw technical profile parameters, 4 raw personal profile parameters, and 1 composite signal score.
* **Training Corpus**: Trained using the Human vs. ChatGPT Comparison Corpus (HC3) to identify structural patterns unique to large language models.

---

## Tech Stack

* **Frontend**: Vanilla JavaScript, HTML5, CSS3 (echo-insight layout)
* **Backend**: FastAPI, Python 3.9, uvicorn
* **Database & Auth**: Supabase, PostgreSQL, JWT Authentication
* **APIs**: Deepgram Nova-2 (Speech-to-Text), Winston AI (Plagiarism & AI Content Verification)

---

## Installation & Setup

### Prerequisites
* Python 3.9 or higher
* Chrome Browser (for extension loading)

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Initialize virtual environment and install packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the backend root:
   ```env
   DEEPGRAM_API_KEY=your-deepgram-api-key
   WINSTON_AI_API_KEY=your-winston-api-key
   SUPABASE_URL=your-supabase-url
   SUPABASE_KEY=your-supabase-key
   JWT_SECRET=your-jwt-secret
   ```
4. Start the server:
   ```bash
   uvicorn server:app --reload --port 8000
   ```

### Chrome Extension Installation
1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode** in the top-right corner.
3. Click **Load unpacked** and select the `chrome-extension/` directory.

---

## License
Distributed under the MIT License. See `LICENSE` for details.
