
# 🚀 Skill Bridge – AI Resume Skill Gap Analyzer

## 👤 Candidate

**Ramayanapu Venkata Pranai**

## 🎯 Scenario

**AI Resume Skill Gap Analyzer**

## ⏱️ Estimated Time Spent

** Video Explanation Link
https://drive.google.com/file/d/1q6fLdwo-te5w_30jtATkjw_Fnkh5y1D1/view?usp=sharing

Approximately **5 hours**

---

## 📌 Project Overview

**Skill Bridge** is an intelligent tool designed to analyze a candidate’s existing skillset and compare it against their target job role. It identifies missing skills and generates a structured, actionable learning roadmap to help bridge the gap.

The goal of this project is to provide clarity and direction for candidates by transforming unstructured resume data into meaningful career insights.

---

## ⚙️ Quick Start Guide

### 🔧 Prerequisites

Make sure the following are installed:

* **Node.js** (v18 or higher)
* **Python** (3.9 or higher)
* Package managers: **pip**, **npm**, or **yarn**

---

## ▶️ Running the Application

### 🔙 Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 🎨 Frontend (React + Tailwind)

```bash
cd frontend/app
npm install
npm run dev
```

---

## 🧪 Testing

Testing was primarily done through manual and API-based approaches:

* **Manual Testing:** Resume upload and text input through the UI
* **API Testing:** Verified endpoints using FastAPI Swagger UI (`/docs`) and browser console

---

## 🤖 AI Usage Disclosure

### Did you use an AI assistant?

Yes. AI was used for:

* Boilerplate code generation
* Logic brainstorming
* Initial API structuring

---

### ✅ How were AI suggestions verified?

* **Manual Validation:** Ensured API responses matched the expected JSON schema
* **Integration Testing:** Resolved issues such as CORS errors, 422 validation failures, and data mismatches
* **Logic Hardening:** Improved AI-generated logic with explicit error handling and required field checks

---

## 🔧 Key Modifications & Rejected Suggestions

* **Architecture:**
  Rejected an approach that tightly coupled frontend rendering with backend response format.
  Implemented a transformation layer in the frontend to normalize roadmap data instead.

* **Robustness:**
  Improved API integration by handling 422 errors explicitly and enforcing role selection.

* **Reliability:**
  Added a fallback mechanism for skill extraction to ensure consistent output even if AI-based parsing fails.

---

## ⚖️ Trade-offs & Limitations

### ⚠️ Known Limitations

* **Accuracy:** Skill extraction relies on AI + fallback logic and may not always be fully accurate
* **Data Constraints:** Roadmap data is static and limited in scope
* **Validation:** No strict validation for malformed or empty resume files
* **Security:** No authentication or session management implemented

---

## ✂️ Features Cut (Time Constraints: 4–6 Hours)

To stay within the time limit, the following were intentionally excluded:

* **Persistence:** No database integration; static data is used
* **Security:** No user authentication or session handling
* **UI Polish:** Minimal animations and basic error feedback

---

## 🚀 Future Improvements

Given more time, the following enhancements would be implemented:

* **Advanced Parsing:**
  Support for PDF/DOCX resumes with improved NLP-based extraction

* **User Profiles:**
  Authentication system to track progress and save roadmaps

* **Dynamic Roadmaps:**
  Integration with platforms like Coursera or Udemy for real-time course recommendations

* **Contextual Matching:**
  Smarter analysis based on work experience, projects, and impact rather than just keywords

* **Deployment:**
  Docker-based containerization for scalable cloud deployment

---

