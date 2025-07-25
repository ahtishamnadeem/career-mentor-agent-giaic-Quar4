from tools import career_tool, skill_tool, job_tool

def career_agent(interest: str) -> str:
    return career_tool(interest)

def skill_agent(field: str) -> str:
    return skill_tool(field)

def job_agent(field: str) -> str:
    return job_tool(field)
