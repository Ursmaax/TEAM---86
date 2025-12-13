from agents.base_agent import Agent
from utils.llm import get_gemini_response

class LogisticsRiskAgent(Agent):
    def __init__(self):
        super().__init__(name="Logistics Risk Agent")

    def run(self, origin: str, destination: str, mode: str) -> str:
        self.clear_logs()
        try:
            self.log_step("Input Received", f"{origin} -> {destination} ({mode})", "Preparing Analysis")
            
            prompt = f"""
            You are the Logistics Risk Agent.
            Analyze QUALITATIVE logistics risks for conditions between {origin} and {destination} via {mode}.
            
            Focus ONLY on:
            - Port congestion / Airport delays
            - Weather disruptions (Seasonality)
            - Piracy or route safety
            - Infrastructure quality
            
            Output Format:
            - Risk Analysis: <Concise analysis>
            - Sources: Simulated sources for demo (e.g., Global Maritime Report, Weather History)
            
            Restrict to general knowledge.
            """
            
            response = get_gemini_response(prompt)
            self.log_step("Analyzed Logistics", "Prompt sent to LLM", "Risk assessment generated")
            
            return response
            
        except Exception as e:
            self.log_step("Error", "LLM Call", str(e))
            return "Unable to analyze logistics risk currently."
