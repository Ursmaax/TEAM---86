from fpdf import FPDF
import os

def create_pdf(report_text, filename="risk_report.pdf"):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="RiskWise Executive Report", ln=1, align='C')
        pdf.ln(10)
        
        # Content
        pdf.set_font("Arial", size=12)
        # Handle unicode issues lightly by replacing common non-ascii
        sanitized_text = report_text.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, txt=sanitized_text)
        
        pdf.output(filename)
        return filename
    except Exception as e:
        print(f"PDF Gen Error: {e}")
        return None
