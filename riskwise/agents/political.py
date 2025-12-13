from agents.base_agent import Agent
from utils.llm import get_gemini_response

class PoliticalRiskAgent(Agent):
    def __init__(self):
        super().__init__(name="Political Risk Agent")

    def run(self, origin: str, destination: str) -> str:
        self.clear_logs()
        try:
            self.log_step("Input Received", f"{origin} -> {destination}", "Preparing Prompt")
            
            prompt = f"""
            You are the Political Risk Agent.
            Analyze political risks for: Origin: {origin}, Destination: {destination}.
            
            Focus ONLY on:
            - Conflicts
            - Protests
            - Government instability
            
            Restrictions:
            - Use general knowledge only (NO real-time search).
            - Be factual and concise.
            
            Output Requirement:
            Ends with a section: "Sources: Simulated sources for demo (e.g., Geopolitical Monitor, Local News)"
            """
            
            response = get_gemini_response(prompt)
            self.log_step("Analyzed Political Tension", "Prompt sent to LLM", "Risk assessment generated")
            
            return response
            
        except Exception as e:
            self.log_step("Error", "LLM Call", str(e))
            return "Unable to analyze political risk currently."
