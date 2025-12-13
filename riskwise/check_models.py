import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

candidates = [
    "gemini-1.5-flash",
    "gemini-pro",
    "gemini-1.5-pro",
    "gemini-1.0-pro",
    "gemini-2.0-flash-exp"
]

if api_key:
    genai.configure(api_key=api_key)
    print("Testing models...")
    for model_name in candidates:
        print(f"Testing {model_name}...", end=" ")
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Hello")
            print("SUCCESS! Response received.")
            with open("working_model.txt", "w") as f:
                f.write(model_name)
            exit(0) # Found one, exit
        except Exception as e:
            print(f"FAILED. Error: {e}")
            
    print("All models failed.")
