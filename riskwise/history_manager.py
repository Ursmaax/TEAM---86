import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"

class HistoryManager:
    @staticmethod
    def save_report(product, origin, destination, final_report, overall_score):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "product": product,
            "origin": origin,
            "destination": destination,
            "risk_score": overall_score,
            "report_preview": final_report[:100] + "..."
        }
        
        history = []
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r") as f:
                    history = json.load(f)
            except:
                pass
                
        history.insert(0, entry) # Prepend
        
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)

    @staticmethod
    def get_history():
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r") as f:
                    return json.load(f)
            except:
                return []
        return []
