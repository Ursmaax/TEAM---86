from agents.base_agent import Agent
from utils.llm import get_gemini_response

class AssistantAgent(Agent):
    def __init__(self):
        super().__init__(name="Assistant Agent")

    def run(self, user_input: str = "Hello") -> str:
        prompt = f"""
        You are the 'Assistant Agent' for RiskWise.
        Your goals:
        1. Handle greetings politely.
        2. Explain that RiskWise analyzes supply chain risks (Political, Trade, Schedule).
        3. Guide the user to enter Product, Origin, Destination, and Dates.
        
        Restrictions:
        - Do NOT perform any risk analysis yourself.
        - Do NOT generate reports.
        - Keep the response short and helpful.
        
        User Input: {user_input}
        """
        return get_gemini_response(prompt)
