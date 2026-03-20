# 🚀 Skill Bridge - AI Resume Skill Gap Analyzer

### **Candidate:** Ramayanapu Venkata Pranai
### **Scenario:** AI Resume Skill Gap Analyzer
### **Estimated Time Spent:** ~5 Hours

---

## 📌 Project Overview
**Skill Bridge** is an intelligent tool designed to bridge the gap between a candidate's current skillset and their target job roles by providing a structured, actionable learning roadmap.

---

## ⚙️ Quick Start Guide

### ● Prerequisites
* **Node.js** (v18+)
* **Python** (3.9+)
* **Package Managers:** `pip`, `npm`, or `yarn`

### ● Run Commands

#### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Frontend (React + Tailwind)
Bash

cd frontend/app
npm install
npm run dev

● Test Commands

    Manual Testing: Resume upload and text input via UI.

    API Testing: Verified via browser console and FastAPI Swagger UI (/docs).

🤖 AI Disclosure & Verification
● Did you use an AI assistant?

Yes. AI was used for boilerplate generation, logic brainstorming, and initial API structuring.
● How did you verify the suggestions?

    Manual Validation: Tested backend API responses for JSON schema compliance.

    Integration Testing: Debugged CORS issues, 422 validation errors, and data structure mismatches.

    Logic Hardening: Refined AI-generated logic to include explicit error handling for required fields.

● Key Modifications & Rejected Suggestions

    Architecture: Rejected an AI-suggested approach that tightly coupled the frontend to the backend response format. Instead, I implemented a transformation layer in the frontend to normalize roadmap data.

    Robustness: Modified API integration to explicitly handle 422 responses and enforce role selection.

    Reliability: Introduced a fallback mechanism for skill extraction to ensure consistent output even if AI-based extraction fails.

⚖️ Tradeoffs & Prioritization
● Known Limitations

    Accuracy: Skill extraction depends on AI + fallback; may not always be 100% accurate.

    Data: Roadmap data is currently static and limited in scope.

    Validation: No current validation for malformed or empty resume files.

    Security: No authentication or user session management.

● What was cut (to stay within the 4–6 hour limit)?

    Persistence: Database integration (used static data instead).

    Security: User accounts and session management.

    Polish: Advanced UI animations and high-fidelity error feedback.

🚀 The Next Horizon

If given more time, the next steps would be:

    Advanced Parsing: Support for PDF/DOCX and enhanced NLP for better extraction.

    User Profiles: Authentication to allow users to save and track their learning progress.

    Dynamic Roadmaps: Integration with external APIs (Coursera/Udemy) for real-time course links.

    Contextual Matching: Matching based on work history and project impact rather than just keywords.

    Deployment: Containerizing the app using Docker for cloud deployment.
