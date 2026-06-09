# Resume-Based Interview Question Generator

An automated candidate screening assistant that analyzes candidate resumes and generates customized, role-specific interview questions. This system assists recruiters by matching technical requirements with candidate experience.

---

## Core Features

### Resume Parsing Engine
* Extracts structured text from resumes (PDF, TXT, or DOCX formats).
* Identifies key headers: Technical Skills, Professional Experience, Education, and Certifications.

### AI-Generated Interview Questions
* Applies advanced prompt engineering to evaluate the candidate's declared projects and skills.
* Generates contextual questions ranging from basic conceptual queries to deep-dive scenario-based questions.
* Formulates expected answers to assist non-technical recruiters in evaluation.

### Recruitment Screening Support
* Provides evaluation rubrics for grading candidate answers.
* Compiles assessments into exportable screening sheets.

---

## Tech Stack
* Language: Python
* Libraries & APIs: OpenAI API / Groq API / NVIDIA API, PyPDF2, python-docx
* Development Tools: Jupyter Notebook, dotenv

---

## Installation & Setup

### Prerequisites
* Python 3.8 or higher
* Active API key for the LLM provider (OpenAI, Groq, or NVIDIA)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/Resume_Based_Interview_Question_Generator.git
   cd Resume_Based_Interview_Question_Generator
   ```

2. Install dependencies:
   ```bash
   pip install pypdf2 python-docx python-dotenv openai requests
   ```

3. Configure environment variables in a `.env` file:
   ```env
   LLM_API_KEY=your-api-key-here
   LLM_MODEL=llama-3-70b-or-similar
   ```

4. Run the script:
   Place the candidate's resume in the `resumes/` directory, then execute:
   ```bash
   python generate_questions.py --resume resumes/candidate_profile.pdf
   ```

---

## License
Distributed under the MIT License. See `LICENSE` for details.
