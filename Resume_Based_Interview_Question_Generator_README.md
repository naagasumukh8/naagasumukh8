# Resume-Based Interview Question Generator

An automated candidate screening assistant that parses applicant profiles and generates customized, role-specific interview questions. This system assists hiring managers and recruiters by evaluating candidates against technical requirements and project declarations.

---

## Core Features

### Profile Analysis Engine
* Extracts structured text from resumes (PDF, TXT, or DOCX formats).
* Groups candidate experience into core technical skills, projects, and educational milestones.

### Contextual Question Generation
* Uses custom prompting logic to evaluate the depth of a candidate's projects and skills.
* Generates conceptual, coding, and behavioral questions tailored to the candidate's background.
* Formulates reference answers and grading guides to assist interviewers.

### Screening Automation
* Evaluates candidate responses against generated reference criteria.
* Generates exportable summary cards for recruiter pipelines.

---

## Tech Stack
* Language: Python
* Integrations: OpenAI API / Groq API / NVIDIA API
* Utilities: PyPDF2, python-docx, python-dotenv

---

## Setup & Installation

### Prerequisites
* Python 3.8 or higher
* Active LLM provider API credentials

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/Resume_Based_Interview_Question_Generator.git
   cd Resume_Based_Interview_Question_Generator
   ```

2. Install python packages:
   ```bash
   pip install pypdf2 python-docx python-dotenv openai requests
   ```

3. Set up environment configurations in a `.env` file:
   ```env
   LLM_API_KEY=your-api-key-here
   LLM_MODEL=llama-3-70b-or-similar
   ```

4. Generate screening questions:
   Place the resume inside the `resumes/` folder, then run:
   ```bash
   python generate_questions.py --resume resumes/candidate_profile.pdf
   ```

---

## License
Distributed under the MIT License. See `LICENSE` for details.
