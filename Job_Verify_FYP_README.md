# Job Verify FYP

A professional credential and employment verification platform designed as a Final Year Project (FYP). It automates and secures the process of verifying candidate qualifications, employment histories, and academic credentials.

---

## Core Features

### Employment Verification Workflow
* Automated verification request queues submitted by candidates or employers.
* Verifier portal for reviewing evidence, contacting references, and updating verification status.
* Status tracking indicators for pending, verified, and flagged applications.

### Secure Credential Repository
* Document upload pipeline for certificates, transcripts, and proof of employment.
* Integrity verification to ensure uploaded files have not been modified post-submission.
* Encryption and role-based access control (RBAC) protecting sensitive files.

### Multi-Role Dashboards
* Candidates: Submit verification profiles, upload documents, and track verification stages.
* Employers: Request checks for prospective hires and view verified candidate credentials.
* Administrators: Manage system settings, review flagged requests, and audit verification actions.

---

## Tech Stack

* Frontend: JavaScript, HTML5, CSS3
* Backend: Node.js, Express, REST APIs
* Database: PostgreSQL / MongoDB
* Version Control: Git, GitHub

---

## Getting Started

### Prerequisites
* Node.js (v18 or higher)
* npm (v9 or higher)
* Database server (PostgreSQL or MongoDB)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/naagasumukh8/Job_Verify_FYP.git
   cd Job_Verify_FYP
   ```

2. Install the backend and frontend dependencies:
   ```bash
   npm install
   ```

3. Configure environment settings by creating a `.env` file in the root directory:
   ```env
   PORT=5000
   DATABASE_URL=your-database-connection-string
   JWT_SECRET=your-json-web-token-secret
   ```

4. Start the application:
   ```bash
   npm start
   ```

---

## Architecture Flow

1. Candidate uploads certificates and inputs previous job roles.
2. Employer initiates a check request.
3. System triggers verification tasks for administrative verifiers.
4. Verifier completes checks, and the status changes to "Verified."
5. Audit logs record all transitions for security tracking.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
