from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import RiskWiseOrchestrator
import os
import uvicorn
from dotenv import load_dotenv

# Load Environment
load_dotenv()

app = FastAPI(title="RiskWise API", version="2.0")

# CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input Model
class RiskRequest(BaseModel):
    product: str
    origin: str
    destination: str
    mode: str
    planned_date: str
    expected_date: str
    demo_mode: bool = False

@app.get("/")
def health_check():
    return {"status": "active", "system": "RiskWise Intelligence Core"}

@app.post("/analyze")
def analyze_risk(request: RiskRequest):
    try:
        # Check API Key if not in demo mode
        if not request.demo_mode and not os.getenv("GROQ_API_KEY"):
             raise HTTPException(status_code=401, detail="API Key Missing")

        orchestrator = RiskWiseOrchestrator()
        
        # Parse Dates
        from datetime import datetime
        try:
            p_date = datetime.strptime(request.planned_date, "%Y-%m-%d").date()
            e_date = datetime.strptime(request.expected_date, "%Y-%m-%d").date()
        except ValueError:
             # Fallback if format is different or standard ISO
             p_date = request.planned_date
             e_date = request.expected_date

        results = orchestrator.analyze_risk(
            product=request.product,
            origin=request.origin,
            destination=request.destination,
            mode=request.mode,
            planned_date=p_date,
            expected_date=e_date,
            demo_mode=request.demo_mode
        )
        
        # Clean results for JSON response (remove non-serializable objects if any)
        # Assuming orchestrator returns dicts/strings/ints which are JSON safe.
        return results

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
