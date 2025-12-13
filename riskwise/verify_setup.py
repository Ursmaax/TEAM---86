import os
import sys
from dotenv import load_dotenv
from orchestrator import RiskWiseOrchestrator
from datetime import date

# Load environment variables
load_dotenv()

def verify_system():
    print("Checking for API Key...")
    if not os.getenv("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY is missing. Please set it in .env or environment.")
        return

    print("Initializing Orchestrator...")
    try:
        orchestrator = RiskWiseOrchestrator()
    except Exception as e:
        print(f"ERROR: Failed to initialize orchestrator: {e}")
        return

    print("Running Test Analysis (Validation Mode Check)...")
    product = "Semiconductors"
    origin = "Taiwan"
    destination = "Germany"
    from datetime import date
    planned = date(2023, 1, 1)
    expected = date(2023, 1, 5)

    try:
        # Note: The verification script uses the simple analyze_risk method
        # which now includes validation.
        results = orchestrator.analyze_risk(product, origin, destination, planned, expected)
        
        print("\n--- TEST RESULTS ---")
        if "Validation Failed" in results.get("final_report", ""):
            print("[CRITICAL]: VALIDATION BLOCKED THE REPORT (This is good if inputs were bad, bad if they were good)")
        
        print("\n[Final Report Preview]")
        print(results["final_report"][:200] + "...")
        
        if "logs" in results:
            print(f"\n[Logs Generated]: {len(results['logs'])} steps recorded.")
            print(f"Sample Log: {results['logs'][0]}")

    except Exception as e:
        print(f"VERIFICATION FAILED: {e}")
        import traceback
        traceback.print_exc()
        
        print("\nVERIFICATION SUCCESSFUL")
        
    except Exception as e:
        print(f"\nERROR: Analysis failed: {e}")

if __name__ == "__main__":
    verify_system()
