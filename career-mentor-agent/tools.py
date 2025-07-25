from utils.gemini import get_field_from_interest, get_skill_roadmap, get_job_roles

def career_tool(interest: str) -> str:
    return get_field_from_interest(interest)

def skill_tool(field: str) -> str:
    return get_skill_roadmap(field)

def job_tool(field: str) -> str:
    return get_job_roles(field)
