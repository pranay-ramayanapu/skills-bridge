from fastapi import FastAPI, File, UploadFile, Form
from services.pdf_parser import extract_text_from_pdf
from services.fallback import extract_skills_fallback
from services.ai_service import extract_skills_ai,refine_with_ai 
from services.utils import get_job, load_courses, find_missing, generate_roadmap
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(
    role: str = Form(...),
    resume_text: str = Form(None),
    file: UploadFile = File(None)
):
    # Step 1: Decide input source
    text = ""

    if file:
        text = extract_text_from_pdf(file.file)

    elif resume_text:
        text = resume_text

    else:
        return {"error": "Provide either resume text or PDF file"}

    if not text.strip():
        return {"error": "Could not extract valid text"}

    # Step 2: AI + fallback
    try:
        user_skills = extract_skills_ai(text)
        # user_skills = ""
        if not user_skills:
            raise Exception("AI failed")
    except Exception as e:
        print("AI failed:", e)
        user_skills = extract_skills_fallback(text)

    # Step 3: Job matching
    job = get_job(role)
    if not job:
        return {"error": "Role not found"}

    # Step 1: rule-based
    missing = find_missing(user_skills, job["skills"])

    # Step 2: AI refinement
    try:
        missing = refine_with_ai(user_skills,job["skills"])
    except:
     pass

    # Step 4: Roadmap
    courses = load_courses()
    roadmap = generate_roadmap(missing, courses)

    return {
        "extracted_skills": user_skills,
        "missing_skills": missing,
        "roadmap": roadmap
    }
