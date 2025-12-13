from agents.base_agent import Agent
from utils.llm import get_gemini_response

class ValidatorAgent(Agent):
    def __init__(self):
        super().__init__(name="Validator Agent")

    def run(self, political_out: str, schedule_out: dict, trade_out: str) -> dict:
        self.clear_logs()
        
        # Rule 1: Check Schedule outputs (Deterministic)
        if "delay_days" not in schedule_out or "risk_level" not in schedule_out:
             self.log_step("Validation Fail", "Schedule Output", "Missing keys")
             return {"valid": False, "reason": "Scheduler Agent failed to produce valid structure."}
             
        # Rule 2: LLM Validation for other agents
        prompt = f"""
        You are a Quality Control Validator.
        Check if these agents followed their strict roles.
        
        Political Agent Output: "{political_out}"
        Trade Agent Output: "{trade_out}"
        
        Rules:
        1. Political Agent MUST discuss conflicts/governments.
        2. Trade Agent MUST discuss tariffs/regulations.
        3. NO new assumptions (hallucinations).
        
        Output "VALID" if ok.
        Output "INVALID: [Reason]" if not.
        """
        
        response = get_gemini_response(prompt)
        self.log_step("Content Validation", "Checking Agent Outputs", response)
        
        if "INVALID" in response:
            return {"valid": False, "reason": response}
            
        return {"valid": True, "reason": "All checks passed"}
