from fastapi import FastAPI
import google.generativeai as genai
from dotenv import load_dotenv
import os
from models import RequestData  

load_dotenv()

app = FastAPI()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

@app.post("/gemini")
async def call_gemini(data: RequestData):
    prompt = f"""
You are an AI disaster alert assistant for blind users.
Based on the following [Disaster Data] and [User Medical Information], generate an emergency warning message tailored to the user's health condition and mobility limitations.
The message should be clear, concise, and formatted in an appropriate tone for voice guidance.

[Disaster Data]
{data.earthquake_data}

[User Medical Information]
{data.user_profile}

Important:
- Emphasize the level of danger.
- Include any specific safety instructions based on the user's mobility or medical conditions.
- The message should be in English, and suitable for audio announcement.
"""

    model = genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content(prompt)
    return {"ai_message": response.text}