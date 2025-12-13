import streamlit as st
import os
import time
from dotenv import load_dotenv
from orchestrator import RiskWiseOrchestrator
import pydeck as pdk
from utils.map_helper import get_coordinates
from history_manager import HistoryManager

# Load environment variables
load_dotenv()

# --- SENSITIVE DATA HANDLING ---
# Streamlit Cloud: Load secrets into os.environ for compatibility with other modules
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

st.set_page_config(page_title="RiskWise AI", page_icon="🌍", layout="wide", initial_sidebar_state="collapsed")

# --- GLOBAL CUSTOM CSS CHECK: INJECTING FIRST ---
st.markdown("""
<style>
    /* VARIABLES */
    :root {
        --bg-main: #0B0F14;
        --bg-card: #121826;
        --accent-primary: #5DA9E9;
        --accent-secondary: #6EE7E0;
        --text-primary: #E6EDF3;
        --text-secondary: #9AA4B2;
        --border-subtle: rgba(255,255,255,0.06);
    }

    /* 1. APPLY GLOBALLY */
    .stApp {
        background-color: var(--bg-main);
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
    }

    /* Container Width strictness */
    .block-container {
        max-width: 100% !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 2rem !important;
        padding-bottom: 5rem !important;
    }

    /* 2. CARD STYLE (MANDATORY) */
    .premium-card {
        background-color: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }

    /* 3. INPUT STYLE */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stDateInput>div>div>input {
        background-color: #171C28 !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        height: 48px;
    }

    /* 4. BUTTON STYLE */
    .stButton > button {
        background-color: var(--accent-primary) !important;
        color: #0B0F14 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 32px !important;
        font-weight: 600 !important;
        width: 100%;
    }

    /* Status Badges */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 12px;
    }
    .status-high { background: rgba(239, 68, 68, 0.15); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2); }
    .status-med { background: rgba(245, 158, 11, 0.15); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.2); }
    .status-low { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.2); }

</style>
""", unsafe_allow_html=True)

def main():
    # --- HEADER SECTION ---
    st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="font-size: 3rem; margin-bottom: 15px; background: linear-gradient(90deg, #E6EDF3, #9AA4B2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">RiskWise AI</h1>
            <p style="font-size: 1.25rem; font-weight: 500; color: #E6EDF3; margin-bottom: 6px;">Deploying autonomous agent swarms to decode global supply chain volatility.</p>
            <p style="font-size: 1.0rem; color: #9AA4B2; opacity: 0.8;">Synthesizing mixed-signal intelligence from political, trade, and logistics vectors.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- SIDEBAR (Internal Logic Only) ---
    with st.sidebar:
        # Keeping functional logic but visual is hidden by default
        demo_toggle = st.toggle("Simulation Mode", value=False)
        api_input = st.text_input("API Key", type="password") if not demo_toggle else None
        if api_input: os.environ["GROQ_API_KEY"] = api_input
        
        # History (Hidden in collapsed sidebar)
        st.markdown("### Recent History")
        history = HistoryManager.get_history()
        for h in history[:3]:
            st.caption(f"{h.get('product')} - {h.get('risk_score')}")

    # --- INPUT CARD ---
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    with st.form("risk_analysis_form"):
        st.markdown("### Assessment Parameters")
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            product = st.text_input("Product / Shipment", value="Semiconductors")
            origin = st.text_input("Origin Point", value="Taiwan")
            planned_date = st.date_input("ETD (Planned)")
        with c2:
            destination = st.text_input("Destination Point", value="Germany")
            mode = st.selectbox("Transport Vector", ["Air Freight", "Sea Freight", "Rail", "Road"])
            expected_date = st.date_input("ETA (Expected)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Initiate Risk Assessment")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PROCESSING & RESULTS ---
    if submitted:
        # Quick validation
        demo_mode = demo_toggle
        if not demo_mode and not os.getenv("GROQ_API_KEY"):
            st.error("API Key Required (Open Sidebar to Configure)")
            return

        with st.spinner("Synthesizing Intelligence..."):
            try:
                orchestrator = RiskWiseOrchestrator()
                results = orchestrator.analyze_risk(
                    product=product, origin=origin, destination=destination,
                    mode=mode, planned_date=planned_date, expected_date=expected_date,
                    demo_mode=demo_mode
                )

                # Parsing Status
                final_text = results["final_report"].lower()
                overall_status = "low"
                if "risk level: high" in final_text: overall_status = "high"
                elif "risk level: medium" in final_text: overall_status = "med"

                status_html = ""
                if overall_status == "high": status_html = '<span class="status-badge status-high">CRITICAL RISK</span>'
                elif overall_status == "med": status_html = '<span class="status-badge status-med">MODERATE RISK</span>'
                else: status_html = '<span class="status-badge status-low">OPERATIONAL</span>'

                # --- SUMMARY CARD ---
                st.markdown(f"""
                <div class="premium-card" style="text-align: center; border-top: 4px solid {'#F87171' if overall_status=='high' else '#FBBF24' if overall_status=='med' else '#34D399'};">
                    {status_html}
                    <h3>Assessment Complete</h3>
                    <div style="text-align: left; margin-top: 20px; color: var(--text-secondary); white-space: pre-line;">
                        {results['final_report']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # --- INTELLIGENCE GRID ---
                st.markdown("### Operational Intelligence")
                row1_col1, row1_col2 = st.columns(2)
                with row1_col1:
                    st.markdown(f'<div class="premium-card"><h4>Political Stability</h4><p>{results.get("political_risk", "")}</p></div>', unsafe_allow_html=True)
                with row1_col2:
                    st.markdown(f'<div class="premium-card"><h4>Schedule Analysis</h4><p>Delay: {results.get("schedule_risk", {}).get("delay_days")} days</p></div>', unsafe_allow_html=True)
                
                row2_col1, row2_col2 = st.columns(2)
                with row2_col1:
                    st.markdown(f'<div class="premium-card"><h4>Trade Compliance</h4><p>{results.get("trade_risk", "")}</p></div>', unsafe_allow_html=True)
                with row2_col2:
                    st.markdown(f'<div class="premium-card"><h4>Logistics & Ops</h4><p>{results.get("logistics_risk", "")}</p></div>', unsafe_allow_html=True)

                # --- MAP VISUALIZATION (FULL WIDTH) ---
                st.markdown("### Geospatial Surveillance")
                st.markdown('<div class="premium-card" style="padding: 0; overflow: hidden;">', unsafe_allow_html=True)
                
                src = get_coordinates(origin)
                dst = get_coordinates(destination)
                
                if src["lat"] != 0 and dst["lat"] != 0:
                    layer = pdk.Layer(
                        "ArcLayer",
                        data=[{"source": [src["lon"], src["lat"]], "target": [dst["lon"], dst["lat"]]}],
                        get_source_position="source", get_target_position="target",
                        get_source_color=[0, 255, 0, 160] if overall_status=="low" else [255, 0, 0, 160],
                        get_target_color=[0, 255, 0, 160] if overall_status=="low" else [255, 0, 0, 160],
                        get_width=6,
                    )
                    view_state = pdk.ViewState(
                        latitude=(src["lat"]+dst["lat"])/2,
                        longitude=(src["lon"]+dst["lon"])/2,
                        zoom=1.5,
                        pitch=30
                    )
                    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, map_style=None), use_container_width=True)
                else:
                    st.warning("Coordinates unavailable for visualization.")
                st.markdown('</div>', unsafe_allow_html=True)

                # --- SCORING & UTILS ---
                # Keeping functionality but moving below map as requested layout "Map (full width)" implies it is a major section
                st.markdown("### Risk Scoring Models")
                if "scores" in results:
                    st.bar_chart(results["scores"])
                    total_score = sum(results["scores"].values())
                    HistoryManager.save_report(product, origin, destination, results["final_report"], total_score)

                # Download
                from utils.pdf_generator import create_pdf
                pdf = create_pdf(results["final_report"])
                if pdf and os.path.exists(pdf):
                    with open(pdf, "rb") as f:
                        st.download_button("Download Report (PDF)", f, "report.pdf", "application/pdf")

            except Exception as e:
                st.error(f"Analysis Interrupted: {str(e)}")

if __name__ == "__main__":
    main()
