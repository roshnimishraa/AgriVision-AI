import io
import tempfile
from datetime import datetime

from fpdf import FPDF


def build_report(cached):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(46, 125, 50)
    pdf.cell(0, 12, "AgriVision AI - Analysis Report", ln=True)

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(0, 6, datetime.now().strftime("Generated %Y-%m-%d %H:%M"), ln=True)
    pdf.ln(4)

    if cached.get("has_photo") and cached.get("image") is not None:
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 8, "Disease Detection", ln=True)

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            cached["image"].convert("RGB").save(tmp.name, format="PNG")
            pdf.image(tmp.name, w=70)

        if cached.get("overlay") is not None:
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp2:
                cached["overlay"].convert("RGB").save(tmp2.name, format="PNG")
                pdf.image(tmp2.name, w=70)

        result = cached["result"]

        pdf.set_font("Helvetica", "", 11)
        pdf.ln(2)
        pdf.cell(0, 7, f"Detected condition: {result['class'].replace('_', ' ')}", ln=True)
        pdf.cell(0, 7, f"Confidence: {result['confidence']*100:.0f}%", ln=True)
        pdf.cell(0, 7, f"Severity score: {result['severity']:.2f}", ln=True)
        pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Yield Forecast", ln=True)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Region: {cached.get('selected_item', '')}", ln=True)
    pdf.cell(0, 7, f"Disease-aware forecast: {cached['fused_pred']:,.0f} hg/ha", ln=True)

    if cached.get("baseline_pred") is not None:
        pdf.cell(
            0,
            7,
            f"If disease ignored: {cached['baseline_pred']:,.0f} hg/ha",
            ln=True
        )

    if cached.get("oracle_pred") is not None:
        pdf.cell(
            0,
            7,
            f"Best-case forecast: {cached['oracle_pred']:,.0f} hg/ha",
            ln=True
        )

    return bytes(pdf.output())
