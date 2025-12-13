from agents.base_agent import Agent
from utils.llm import get_gemini_response

class TradeRiskAgent(Agent):
    def __init__(self):
        super().__init__(name="Trade Risk Agent")

    def run(self, product: str, origin: str, destination: str) -> str:
        self.clear_logs()
        try:
            self.log_step("Input Received", f"Product: {product}, Path: {origin}->{destination}", "Preparing Prompt")
            
            prompt = f"""
            You are the Trade Risk Agent.
            Analyze trade/regulatory risks for: Product: {product}, Origin: {origin}, Destination: {destination}.
            
            Focus ONLY on:
            - Import/export restrictions
            - Tariff sensitivity and trade barriers
            
            Keep it concise.
            
            Output Requirement:
            Ends with a section: "Sources: Simulated sources for demo (e.g., WTO Database, Trade Ministry)"
            """
            
            response = get_gemini_response(prompt)
            self.log_step("Identified Trade Barriers", "Prompt sent to LLM", "Trade analysis generated")
            
            return response
            
        except Exception as e:
            self.log_step("Error", "LLM Call", str(e))
            return "Unable to analyze trade risk currently."
