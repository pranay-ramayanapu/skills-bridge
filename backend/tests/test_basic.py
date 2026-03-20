from services.utils import find_missing

def test_gap():
    user = ["Python", "SQL"]
    job = ["Python", "SQL", "Spark"]
    assert find_missing(user, job) == ["Spark"]

def test_empty():
    from services.fallback import extract_skills_fallback
    assert extract_skills_fallback("") == []
