from agents.base_agent import Agent
from utils.llm import get_gemini_response

class ReportingAgent(Agent):
    def __init__(self):
        super().__init__(name="Reporting Agent")

    def run(self, political_risk: str, schedule_risk: dict, trade_risk: str, logistics_risk: str) -> str:
        self.clear_logs()
        try:
            self.log_step("Aggregating Inputs", "Received reports including Logistics", "Preparing Final Summary Prompt")
            
            prompt = f"""
            You are the Reporting Agent.
            Combine these inputs into a final report.
            
            Inputs:
            1. Political Risk: {political_risk}
            2. Schedule Risk: Delay {schedule_risk['delay_days']} days, Level {schedule_risk['risk_level']}
            3. Trade Risk: {trade_risk}
            4. Logistics Risk (Qualitative): {logistics_risk}
            
            STRICT RULES FOR OVERALL RISK:
            - If ANY input is 'High' risk -> Overall Risk is HIGH.
            - Else if ANY input is 'Medium' risk -> Overall Risk is MEDIUM.
            - Else -> Overall Risk is LOW.
            
            REQUIRED FORMAT:
            
            Executive Summary:
            - Overall Risk Level: <Low | Medium | High>

            Key Reasons:
            - Schedule: <1 sentence summary>
            - Political: <1 sentence summary>
            - Trade: <1 sentence summary>
            - Logistics: <1 sentence summary>

            Recommendation:
            - <One clear action in simple English>
            """
            
            response = get_gemini_response(prompt)
            self.log_step("Generated Executive Summary", "Prompt sent to LLM", "Final Report Created")
            return response
            
        except Exception as e:
            self.log_step("Error", "Summary Generation", str(e))
            return "Unable to generate final report."
