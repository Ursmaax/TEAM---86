import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

print(f"Key loaded: {api_key[:5]}...")

try:
    print("Initializing client...")
    client = Groq(api_key=api_key)
    print("Client initialized. Sending request...")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain AI in 10 words",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print(chat_completion.choices[0].message.content)
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
