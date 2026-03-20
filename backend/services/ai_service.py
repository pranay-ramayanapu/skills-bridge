import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_skills_ai(text):
    try:
        prompt = f"""
        Extract only technical skills from the text below.
        Return ONLY a comma-separated list.
        No explanation, no extra words.

        Text:
        {text}
        """

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        if not response.text:
            return []

        skills = [s.strip() for s in response.text.split(",")]

        return skills

    except Exception as e:
        print("AI Error:", e)
        return []
def refine_with_ai(user_skills, job_skills):
    try:
        prompt = f"""
        You are given two lists:

        User Skills: {user_skills}
        Required Skills: {job_skills}

        Identify which required skills are missing.
        Consider similar skills (e.g., MongoDB = Databases).

        Return ONLY a comma-separated list of missing skills.
        No explanation.
        """

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        if not response.text:
            return []

        return [s.strip() for s in response.text.split(",")]

    except:
        return []
