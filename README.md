# Skill Bridge - Resume Analyzer

## Candidate Name:
Ramayanapu Venkata Pranai

## Scenario Chosen:
AI Resume Skill Gap Analyzer

## Estimated Time Spent:
~5 hours

---

## Quick Start:

### ● Prerequisites:
- Node.js (v18+)
- Python (3.9+)
- pip / virtualenv
- npm or yarn

---

### ● Run Commands:

#### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

#### Frontend (React+Tailwind)
cd frontend/app
npm install
npm run dev

### ● Test Commands:
Manual testing via UI (resume upload / text input)
API tested through browser and console logs

AI Disclosure:
### ● Did you use an AI assistant (Copilot, ChatGPT, etc.)?

-Yes

### ● How did you verify the suggestions?

-Tested backend API responses manually

-Verified frontend-backend integration

-Debugged errors such as CORS issues, 422 validation errors, and data structure mismatches

### ● Give one example of a suggestion you rejected or changed:
- Rejected an AI-suggested approach that tightly coupled frontend rendering with backend response format. Instead, implemented a transformation layer in the frontend to normalize roadmap data, making the UI resilient to backend changes.

- Modified AI-generated API integration logic to explicitly handle validation errors (422 responses) and enforce required fields like role selection, improving overall robustness of the system.

- Refined skill extraction handling by introducing a fallback mechanism when AI-based extraction fails, ensuring consistent output instead of relying solely on AI responses.

### ● Tradeoffs & Prioritization:
### ● Known limitations:

-Skill extraction depends on AI + fallback, may not always be accurate

-Roadmap data is static and limited

-No validation for malformed or empty resumes

-No authentication or user session management

-UI does not handle all edge cases gracefully

### ● What did you cut to stay within the 4–6 hour limit?

-Authentication and user accounts

-Database integration (used static data instead)

-Advanced UI polish and animations

-Robust error handling and validation

### ● What would you build next if you had more time?

- Implement user authentication and session management to allow users to save and track their analysis results  

- Improve resume parsing by supporting multiple formats (PDF, DOCX) and enhancing extraction accuracy using better NLP techniques  

- Add multiple resume input methods (file upload, direct text, LinkedIn/profile import) for flexibility  

- Introduce advanced matching beyond skills, including project experience, work history, and contextual relevance  

- Build a job-role matching system that suggests suitable roles based on the user's profile  

- Enhance the roadmap by including real course links, learning paths, and progress tracking  

- Improve UI/UX with loading states, better feedback, and visual indicators like match scores or progress bars  

- Prepare the application for deployment using Docker and cloud infrastructure
