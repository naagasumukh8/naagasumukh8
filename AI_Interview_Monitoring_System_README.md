# AI Interview Monitoring System

An intelligent audio and speech processing pipeline designed to monitor and assist during remote technical interviews. This system detects plagiarism and aids recruiters by verifying candidate speech patterns and content during live screenings.

---

## Core Features

### Audio Capture & Processing
* Real-time audio recording interface capturing candidate responses.
* Noise reduction filters to optimize audio quality before processing.

### Speech-to-Text Pipeline
* Integration with speech recognition APIs to transcribe audio responses into structured text files.
* Timestamp synchronization for mapping text segments to specific parts of the interview.

### Plagiarism and Assistance Verification
* Natural Language Processing algorithms to analyze transcript similarities against online documentation, question databases, or pre-written answers.
* Prompt-based assessment metrics to detect anomalies in speech response structure.

---

## Tech Stack
* Language: Python
* Frameworks/APIs: SpeechRecognition, PyAudio, Web APIs (Speech-to-Text engines)
* Scripting & Logic: Scripting workflows for file saving, API querying, and result generation

---

## Installation & Setup

### Prerequisites
* Python 3.9 or higher
* Working microphone and audio input configurations

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/AI_Interview_Monitoring_System.git
   cd AI_Interview_Monitoring_System
   ```

2. Install system requirements:
   On Windows, you may need to install PyAudio. If binary compilation is required, use precompiled wheels or pip:
   ```bash
   pip install SpeechRecognition pyaudio requests
   ```

3. Configure API credentials:
   If using external speech engines or LLMs, configure keys in a `.env` file:
   ```env
   SPEECH_API_KEY=your-api-key-here
   ```

4. Run the application:
   ```bash
   python monitor.py
   ```

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
