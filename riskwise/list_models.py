import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("No API Key found")
else:
    genai.configure(api_key=api_key)
    with open("c:/New Peoject/available_models.txt", "w") as f:
        try:
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    f.write(m.name + "\n")
                    print(m.name)
        except Exception as e:
            f.write(f"Error listing models: {e}\n")
            print(f"Error: {e}")
