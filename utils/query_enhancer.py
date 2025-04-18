import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() 

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def enhance_query(raw_query):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Improve and expand this job query to match it with SHL assessments. Be specific and clear.\n\nQuery: \"{raw_query}\""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini Error:", e)
        return raw_query 
