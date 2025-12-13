import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
# The client will automatically look for GROQ_API_KEY in environment
# but we can also pass it explicitly if managed by the app
def get_groq_client(api_key=None):
    if api_key:
        return Groq(api_key=api_key)
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_gemini_response(prompt: str, model_name: str = "llama-3.3-70b-versatile", api_key: str = None) -> str:
    """
    Generates a response using Groq (Previously named get_gemini_response for compatibility).
    Keeping function name same to avoid refactoring all agents immediately, 
    but strictly it calls Groq.
    
    Args:
        prompt (str): The prompt to send.
        model_name (str): Defaults to llama3-8b-8192.
        api_key (str): Optional API key override.
        
    Returns:
        str: Response text.
    """
    try:
        client = get_groq_client(api_key)
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model_name,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq: {str(e)}"
