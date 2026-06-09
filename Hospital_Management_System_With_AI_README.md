# Hospital Management System with AI

A comprehensive hospital operations and patient management platform designed to streamline doctor scheduling, clinic admin workflows, and patient triage through integrated artificial intelligence features.

---

## Core Features

### Patient Triage and AI Assistance
* Automated symptom checking and department recommendations.
* AI-assisted chatbot for handling patient queries and booking procedures.
* Smart filtering for identifying medical emergencies.

### Appointment Scheduling
* Dynamic scheduling algorithm for doctor slots, preventing double bookings.
* Patient portal for booking, rescheduling, and viewing appointment status.
* Automated notification queue for status changes.

### Medical Records Management
* Secure storage for patient profiles, medical histories, and digital prescriptions.
* Structured timeline displaying patient visits, diagnostic tests, and follow-ups.
* Role-based access control protecting patient privacy.

---

## Tech Stack

* Frontend: React, JavaScript, CSS3
* Backend & Server: Node.js, Express, REST APIs
* Database: Supabase / PostgreSQL (with Row Level Security)
* AI Engines: NVIDIA API / Groq API (Llama models)
* Build & Package Manager: npm

---

## Installation & Setup

### Prerequisites
* Node.js (v18 or higher)
* npm (v9 or higher)
* A Supabase project and database instance

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/Hospital_Management_System_With_AI.git
   cd Hospital_Management_System_With_AI
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables. Create a `.env` file in the root directory:
   ```env
   SUPABASE_URL=your-supabase-url
   SUPABASE_ANON_KEY=your-supabase-anon-key
   AI_API_KEY=your-nvidia-or-groq-key
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

---

## Contributing
Contributions are welcome. Please follow the standard development workflow:
1. Fork the project.
2. Create a feature branch: `git checkout -b feature/amazing-feature`.
3. Commit your changes: `git commit -m "Add amazing feature"`.
4. Push to the branch: `git push origin feature/amazing-feature`.
5. Open a Pull Request.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
