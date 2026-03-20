import re

SKILL_PATTERNS = {
    # Programming Languages
    "Python": [r"\bpython\b"],
    "Java": [r"\bjava\b"],
    "JavaScript": [r"\bjavascript\b", r"\bjs\b"],
    "C++": [r"\bc\+\+\b"],
    "C": [r"\bc\b"],

    # Databases
    "SQL": [r"\bsql\b"],
    "MySQL": [r"\bmysql\b"],
    "PostgreSQL": [r"\bpostgresql\b", r"\bpostgres\b"],
    "MongoDB": [r"\bmongodb\b", r"\bnosql\b"],
    "Databases": [r"\bdatabase[s]?\b", r"\bdb\b"],

    # Backend
    "Node.js": [r"\bnode\.?js\b", r"\bnode\b"],
    "REST APIs": [r"\brest\b", r"\bapi[s]?\b"],
    "Microservices": [r"\bmicroservice[s]?\b"],
    "Authentication": [r"\bauth\b", r"\bauthentication\b", r"\boauth\b"],

    # Frontend
    "React": [r"\breact\b", r"\breactjs\b"],
    "HTML": [r"\bhtml\b"],
    "CSS": [r"\bcss\b"],
    "Responsive Design": [r"\bresponsive\b"],
    "Redux": [r"\bredux\b"],

    # Data Engineering
    "ETL": [r"\betl\b", r"\bdata pipeline[s]?\b", r"\bingestion\b"],
    "Apache Spark": [r"\bspark\b"],
    "Data Warehousing": [r"\bdata warehouse\b"],
    "Airflow": [r"\bairflow\b"],

    # Cloud
    "AWS": [r"\baws\b", r"\bamazon web services\b"],
    "Azure": [r"\bazure\b"],
    "GCP": [r"\bgcp\b", r"\bgoogle cloud\b"],
    "Cloud": [r"\bcloud\b"],

    # DevOps
    "Docker": [r"\bdocker\b", r"\bcontainer[s]?\b"],
    "Kubernetes": [r"\bkubernetes\b", r"\bk8s\b"],
    "CI/CD": [r"\bci/cd\b", r"\bcontinuous integration\b"],
    "Terraform": [r"\bterraform\b"],
    "Linux": [r"\blinux\b"],
    "Bash": [r"\bbash\b", r"\bshell\b"],

    # ML / AI
    "TensorFlow": [r"\btensorflow\b"],
    "PyTorch": [r"\bpytorch\b"],
    "Scikit-learn": [r"\bscikit\b", r"\bsklearn\b"],
    "Machine Learning": [r"\bmachine learning\b", r"\bml\b"],
    "Deep Learning": [r"\bdeep learning\b"],
    "NLP": [r"\bnlp\b", r"\bnatural language processing\b"],

    # Tools
    "Git": [r"\bgit\b", r"\bgithub\b"],
    "Firebase": [r"\bfirebase\b"],

    # Frameworks
    "Django": [r"\bdjango\b"],
    "Spring Boot": [r"\bspring\s?boot\b"],
    "Flutter": [r"\bflutter\b"],
    "Kotlin": [r"\bkotlin\b"],
    "Swift": [r"\bswift\b"],

    # Testing
    "Selenium": [r"\bselenium\b"],
    "JUnit": [r"\bjunit\b"],
    "Testing": [r"\btesting\b", r"\btest automation\b"],

    # Security
    "Cybersecurity": [r"\bsecurity\b", r"\bcyber\b"],
    "Cryptography": [r"\bcryptography\b"],
    "SIEM": [r"\bsiem\b"]
}

def extract_skills_fallback(text):
    text = text.lower()
    found_skills = set()

    for skill, patterns in SKILL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                found_skills.add(skill)
                break

    return list(found_skills)
