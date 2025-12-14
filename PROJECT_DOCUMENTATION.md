# Project Documentation: RiskWise AI

## 1. Project Overview
RiskWise AI is a software tool designed to help supply chain managers predict logistics risks. It uses Artificial Intelligence to analyze political, weather, and trade data in real-time. This tool is built for logistics companies who need to know about shipment delays into the future, rather than reacting to them after they happen.

## 2. Problem Statement
Global supply chains are fragile. Unexpected events like severe storms, port strikes, or new government trade laws can delay shipments for weeks.
*   **Example**: A ship carrying electronics from Taiwan to Germany might get stuck due to a sudden tariff change or a typhoon.
Currently, companies only find out about these problems after the delay has already started. This leads to lost revenue and unhappy customers. There is a lack of simple tools that provide early warnings.

## 3. Solution Overview
RiskWise solves this problem by predicting risks in advance. It acts as an intelligent "Command Center" that monitors global data 24/7.
Instead of requiring a human to read news and check weather reports manually, our system uses AI Agents to do this work automatically. The system provides a unified "Risk Score" and a detailed explanation for every shipment, allowing managers to change routes or plans proactively.

## 4. System Architecture
The system follows a linear data flow to process requests:
1.  **Input**: The user inputs shipment details (Origin, Destination, Product, Transport Mode).
2.  **Orchestrator**: The central controller (RiskWiseOrchestrator) receives this data and validates it.
3.  **Agent Delegation**: The Orchestrator sends specific tasks to three specialized AI Agents (Political, Logistics, and Trade).
4.  **Parallel Processing**: All agents analyze the data simultaneously using the Groq AI engine.
5.  **Aggregation**: The Orchestrator collects the answers from all agents.
6.  **Final Output**: The system calculates a cumulative Risk Score and generates a final report for the user interface.

## 5. AI & Multi-Agent Design
We utilize a Multi-Agent Architecture to ensure high accuracy. Instead of one general AI, we use specialized agents:
*   **Political Agent**: Analyzes government stability, sanctions, and conflict risks.
*   **Logistics Agent**: Analyzes weather patterns, port congestion, and route disruptions.
*   **Trade Agent**: Analyzes tariffs, customs regulations, and compliance rules.

**Why Multiple Agents?**
Complex problems require focused expertise. By splitting the task, each agent can go deeper into its specific topic without getting confused by unrelated data. We use Generative AI (LLM) to synthesize this complex technical data into simple, readable text.

## 6. Technology Stack
*   **Python**: The core programming language used for all logic and data processing. It was chosen for its strong support for AI libraries.
*   **Streamlit**: A framework for building the web user interface. We chosen it because it allows for rapid development of data-centric dashboards without complex frontend code.
*   **Groq**: The AI inference engine. We chosen Groq because of its ultra-low latency (speed). It allows our specific coding agents to "think" and respond in milliseconds.
*   **Pydeck**: A library for geospatial visualization. It is used to render the 3D map of the shipping route.

## 7. User Workflow
1.  **Access**: The user opens the web application in a browser.
2.  **Input**: The user enters the "Origin" (e.g., Shanghai) and "Destination" (e.g., Hamburg) cities.
3.  **Execute**: The user clicks the "Initiate Risk Assessment" button.
4.  **Processing**: The system displays a status indicator while the agents perform the analysis.
5.  **Review**: The user views the final dashboard, which includes the Risk Score, Interactive Map, and detailed Agent Reports.
6.  **Export**: The user can download the full analysis as a PDF file.

## 8. Output & Reporting
The application provides three key outputs:
*   **Risk Score**: A quantitative score from 0 to 100. A score of 0-20 indicates low risk, while 70+ indicates critical risk.
*   **Map Visualization**: A visual representation of the trade route on a global map, helping users verify the geography.
*   **PDF Report**: A professional document containing all findings, suitable for sharing with executive teams.

## 9. Deployment
The application is deployed on **Streamlit Cloud**.
**Why this approach?**
Streamlit Cloud integrates directly with our GitHub repository. This ensures Continuous Deployment (CD). Whenever the development team pushes code changes to GitHub, the live application updates automatically within minutes. This is critical for maintaining up-to-date availability during the project lifecycle.

## 10. Limitations & Future Improvements
**Current Limitations**:
*   **Coordinate Data**: The demo version uses a static database for map coordinates, covering major global hubs but not every small city.
*   **Real-time Data**: The AI relies on its training data and simulated live inputs; it does not yet connect to a live maritime tracking API (like MarineTraffic).

**Future Improvements**:
*   Integrate real-time satellite AIS data for live vessel tracking.
*   Add a "Financial Risk" agent to estimate monetary loss.
*   Implement user accounts to save search history.

## 11. Team Information
**Team 86**
*   Project Lead
*   Developer
*   Researcher
*   Designer

---
*Document Date: December 14, 2025*
