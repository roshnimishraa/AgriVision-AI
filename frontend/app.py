"""
AgriVision AI — Streamlit entrypoint.

A navbar (src/ui/theme.py: navbar()) switches between two views using
st.session_state, not a real multipage app -- simpler and version-independent:
    - "about": src/ui/about_page.py -- static project description
    - "tool":  src/ui/unified_page.py -- the actual product (default)

    src/config.py               -- every file path + constant, in one place
    src/model_loader.py         -- cheap existence checks + independently cached loaders
    src/disease_detection.py    -- CNN preprocessing + prediction
    src/grad_cam.py             -- disease-side explainability (heatmap), cached graph
    src/yield_prediction.py     -- feature building + RF prediction, per model variant
    src/yield_explainability.py -- yield-side explainability (live SHAP)
    src/report_generator.py     -- downloadable PDF summary
    src/ui/theme.py             -- page config + styling + navbar
    src/ui/about_page.py        -- About page
    src/ui/unified_page.py      -- the entire tool, as one flow

Run with:  streamlit run app.py
"""

import streamlit as st

from src.ui import theme, about_page, unified_page

theme.apply()
theme.navbar()

if st.session_state.get("current_page") == "about":
    about_page.render()
else:
    
    unified_page.render()
