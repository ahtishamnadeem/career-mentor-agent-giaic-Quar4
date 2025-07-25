import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Get Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

def get_field_from_interest(interest: str) -> str:
    prompt = f"Suggest the most suitable career field for someone interested in {interest}."
    return model.generate_content(prompt).text

def get_skill_roadmap(field: str) -> str:
    prompt = f"Give a step-by-step skill building roadmap to succeed in the field of {field}."
    return model.generate_content(prompt).text

def get_job_roles(field: str) -> str:
    prompt = f"List 5 real-world job roles someone can pursue in the field of {field}."
    return model.generate_content(prompt).text
