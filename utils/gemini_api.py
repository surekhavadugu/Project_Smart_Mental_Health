# utils/gemini_api.py
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_gemini_answer(prompt):
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("GEMINI_API_KEY not found in .env file")
            return "Error: API key missing."

        # Configure Gemini API
        genai.configure(api_key=api_key)

        # Create the model
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Generate response
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f" Gemini API Error: {e}")
        return "Error: Could not get response from Gemini API."
