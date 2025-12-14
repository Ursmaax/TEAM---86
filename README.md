# RiskWise AI

**Global Supply Chain Intelligence Platform**

RiskWise AI is a multi-agent system designed to predict and mitigate supply chain disruptions before they occur. By analyzing real-time geopolitical, weather, and trade data, it provides actionable foresight for logistics operations.

---

### 🔗 Essential Links

*   **[🚀 Launch Live Application](https://team---86-rnw5sqr6qkcfxcgpkdsfms.streamlit.app)** - Run the app immediately in your browser.
*   **[📺 Watch Demo Video](https://youtu.be/etLvSZD4GKo)** - See the comprehensive workflow walkthrough.
*   **[📄 Project Documentation](PROJECT_DOCUMENTATION.md)** - Detailed technical architecture and design.

---

## Project Overview

**The Problem**
Logistics teams often react to disruptions (port strikes, storms, regulations) only after they occur, leading to significant financial loss and delays.

**The Solution**
RiskWise uses a swarm of autonomous AI agents to monitor global risks 24/7. It acts as an intelligent command center that predicts delays, explains regulatory changes, and scores the safety of every shipment in real-time.

## How It Works

The system operates using a Multi-Agent Architecture powered by `Groq` for ultra-fast inference:

1.  **Input**: User defines a shipment route (e.g., "Electronics from Taiwan to Germany").
2.  **Analysis**:
    *   **Political Agent**: Evaluates geopolitical stability and sanctions.
    *   **Logistics Agent**: Checks weather conditions and port congestion.
    *   **Trade Agent**: Analyzes tariffs and compliance requirements.
3.  **Output**: A unified **Risk Score (0-100)** and a comprehensive PDF Report explanation.

## Technology Stack

*   **Python**: Core logic and orchestration.
*   **Groq LPU**: High-speed AI inference.
*   **Streamlit**: User interface and dashboard.
*   **Pydeck**: Geospatial route visualization.

## Run Locally

To install and run the project on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/Ursmaax/TEAM---86.git
cd TEAM---86

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run riskwise/app.py
```

## Team 86

*   **Umamahesh** - Project Lead
*   **Karthik Manikanta**
*   **Jaya Vardhini**
*   **Harshini**

*Submitted for JNTUGV GenAI Hackathon 2025.*
