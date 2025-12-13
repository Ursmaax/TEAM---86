from riskwise.utils.llm import get_gemini_response
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
print(f"Key loaded: {key[:5]}...{key[-3:] if key else 'None'}")

print("Sending request...")
response = get_gemini_response("Hello")
print(f"RESPONSE: {response}")
