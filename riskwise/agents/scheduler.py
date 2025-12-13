from agents.base_agent import Agent
from datetime import date

class SchedulerAgent(Agent):
    def __init__(self):
        super().__init__(name="Scheduler Agent")

    def run(self, planned_date: date, expected_date: date) -> dict:
        self.clear_logs()
        try:
            self.log_step("Input Received", f"Planned: {planned_date}, Expected: {expected_date}", "Parsing dates")
            
            delay_days = (expected_date - planned_date).days
            self.log_step("Calculated Delay", f"{expected_date} - {planned_date}", f"{delay_days} days")
            
            risk_level = "Low"
            if delay_days > 10:
                risk_level = "High"
            elif delay_days >= 4:
                risk_level = "Medium"
            elif delay_days <= 3:
                risk_level = "Low"
            
            self.log_step("Assessed Risk Level", f"Delay: {delay_days}", f"Risk: {risk_level}")
                
            result = {
                "delay_days": delay_days,
                "risk_level": risk_level,
                "description": f"Delay of {delay_days} days detected. Risk is {risk_level}."
            }
            return result
            
        except Exception as e:
            self.log_step("Error", "Processing Dates", str(e))
            return {
                "delay_days": 0,
                "risk_level": "Unknown",
                "description": "Error processing schedule."
            }
