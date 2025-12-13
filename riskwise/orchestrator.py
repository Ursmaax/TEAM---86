from agents.political import PoliticalRiskAgent
from agents.scheduler import SchedulerAgent
from agents.trade import TradeRiskAgent
from agents.reporting import ReportingAgent
from agents.assistant import AssistantAgent

from agents.validator import ValidatorAgent

from agents.logistics import LogisticsRiskAgent

class RiskWiseOrchestrator:
    def __init__(self):
        self.political_agent = PoliticalRiskAgent()
        self.scheduler_agent = SchedulerAgent()
        self.trade_agent = TradeRiskAgent()
        self.logistics_agent = LogisticsRiskAgent() # New Agent
        self.reporting_agent = ReportingAgent()
        self.assistant_agent = AssistantAgent()
        self.validator_agent = ValidatorAgent()

    # ... (rest of methods)

    def analyze_risk(self, product: str, origin: str, destination: str, mode: str, planned_date, expected_date, demo_mode: bool = False):
        print(f"Starting FINAL analysis for {product} from {origin} to {destination} via {mode} (Demo: {demo_mode})")
        
        if demo_mode:
            return self._run_demo_mode()

        # 1. SCHEDULER AGENT
        schedule_risk = self.scheduler_agent.run(planned_date, expected_date)
        
        # 2. POLITICAL RISK AGENT
        political_risk = self.political_agent.run(origin, destination)
        
        # 3. TRADE RISK AGENT
        trade_risk = self.trade_agent.run(product, origin, destination)
        
        # 4. LOGISTICS RISK AGENT (Qualitative)
        logistics_risk = self.logistics_agent.run(origin, destination, mode)
        
        # 5. REPORTING AGENT
        final_report = self.reporting_agent.run(political_risk, schedule_risk, trade_risk, logistics_risk)
        
        # SCORING (Numeric 1-5)
        scores = self._calculate_scores(political_risk, schedule_risk, trade_risk, logistics_risk)

        # VALIDATION (Safety Check)
        validation = self.validator_agent.run(political_risk, schedule_risk, trade_risk)
        # Note: We aren't strictly validating logistics yet to keep it simple, or we can add it.
        
        if not validation["valid"]:
             final_report = f"### Error: Validation Failed\n{validation['reason']}"
        
        logs = (self.scheduler_agent.get_logs() + 
                self.political_agent.get_logs() + 
                self.trade_agent.get_logs() + 
                self.logistics_agent.get_logs() +
                self.reporting_agent.get_logs())
        
        return {
            "political_risk": political_risk,
            "schedule_risk": schedule_risk,
            "trade_risk": trade_risk,
            "logistics_risk": logistics_risk,
            "final_report": final_report,
            "scores": scores,
            "logs": logs
        }

    def _calculate_scores(self, pol_out, sched_out, trade_out, log_out):
        # Heuristic scoring
        def text_to_score(text):
            text = str(text).lower()
            if "high" in text: return 5
            if "medium" in text: return 3
            return 1
            
        p_score = text_to_score(pol_out)
        s_score = text_to_score(sched_out.get('risk_level', 'Low'))
        t_score = text_to_score(trade_out)
        l_score = text_to_score(log_out)
        
        return {"Political": p_score, "Schedule": s_score, "Trade": t_score, "Logistics": l_score}

    def _run_demo_mode(self):
        return {
            "political_risk": "Demo: Low political tension observed in the region.",
            "schedule_risk": {"delay_days": 2, "risk_level": "Low", "description": "Demo: Minor delays."},
            "trade_risk": "Demo: Standard tariffs apply. No sanctions.",
            "final_report": """Executive Summary:
- Overall Risk Level: Low

Key Reasons:
- Schedule: On time.
- Political: Stable.
- Trade: Normal.

Recommendation:
- Proceed with shipment.""",
            "scores": {"Political": 1, "Schedule": 2, "Trade": 1},
            "logs": [{"agent": "System", "step": "Demo Mode", "input": "N/A", "output": "Simulated Response"}]
        }
