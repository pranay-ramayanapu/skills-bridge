import json

def load_jobs():
    with open("data/jobs.json") as f:
        return json.load(f)

def load_courses():
    with open("data/courses.json") as f:
        return json.load(f)

def get_job(role):
    jobs = load_jobs()
    for job in jobs:
        if job["role"].lower() == role.lower():
            return job
    return None
def find_missing(user_skills, job_skills):
    return list(set(job_skills) - set(user_skills))

def generate_roadmap(missing_skills, courses):
    roadmap = []
    normalized_courses = {k.lower(): v for k, v in courses.items()}

    for skill in missing_skills:
        key = skill.lower().strip()

        # direct match
        if key in normalized_courses:
            roadmap.append({
                "skill": skill,
                **normalized_courses[key][0]
            })
            continue
        SKILL_MAP = {
            # Databases / SQL
            "sql": ["mysql", "postgresql"],
            "databases": ["mysql", "postgresql", "mongodb"],
            "rdbms": ["mysql", "postgresql"],
            "nosql": ["mongodb"],
    
            # Backend / APIs
            "rest apis": ["rest api"],
            "api": ["rest api"],
            "apis": ["rest api"],
            "backend": ["node.js", "django", "springboot"],
            "authentication": ["oauth2"],
    
            # Frontend
            "react": ["reactjs"],
            "frontend": ["reactjs", "javascript"],
            "ui": ["reactjs"],
            "javascript": ["javascript"],
            "js": ["javascript"],
    
            # Programming languages
            "python": ["python"],
            "java": ["java"],
            "c++": ["c++"],
            "c": ["c"],
    
            # DevOps / Cloud
            "devops": ["docker", "kubernetes"],
            "containers": ["docker"],
            "containerization": ["docker"],
            "orchestration": ["kubernetes"],
                "ci/cd": ["docker"],  # weak mapping but acceptable for now
            "linux": ["bash"],
            "shell": ["bash"],
            "scripting": ["bash"],
    
            # Data Engineering
            "etl": ["etl"],
            "data pipelines": ["etl"],
            "big data": ["spark"],
            "apache spark": ["spark"],
    
            # Frameworks
            "node": ["node.js"],
            "nodejs": ["node.js"],
            "express": ["node.js"],  # indirect but practical
            "django": ["django"],
            "spring": ["springboot"],
            "spring boot": ["springboot"],
    
            # Version control
            "version control": ["git"],
            "git": ["git"],
            "github": ["git"]
        }

        # mapped match
        if key in SKILL_MAP:
            for mapped in SKILL_MAP[key]:
                if mapped in normalized_courses:
                    roadmap.append({
                        "skill": skill,
                        **normalized_courses[mapped][0]
                    })
                    break

    return roadmap
