"""
Reusable UI components for AgriVision AI.

Every function here only renders — none of them decide what state the
app is in. Callers (about_page.py, unified_page.py) pass in whatever
state they need shown (e.g. which step is current); components.py
never reaches into st.session_state itself. That keeps this file easy
to reuse and test on its own.
"""

import os
import streamlit as st

from src import config
from src.ui.html_utils import render_html


# def navbar():
#     """Top navigation bar. Sets the current_page default and renders
#     the Home / Tool nav buttons."""

#     if "current_page" not in st.session_state:
#         st.session_state["current_page"] = "about"

#     logo, home, tool, blank = st.columns([1.5, 0.8, 0.8, 0.1])

#     with logo:
#         render_html('<div class="avi-logo">AgriVision AI</div>')

#     with home:
#         if st.button(
#             "Home",
#             key="home_nav",
#             use_container_width=True,
#             type="primary" if st.session_state["current_page"] == "about" else "secondary",
#         ):
#             st.session_state["current_page"] = "about"
#             st.rerun()

#     with tool:
#         if st.button(
#             "Crop Disease Detection & Yield Prediction",
#             key="tool_nav",
#             use_container_width=True,
#             type="primary" if st.session_state["current_page"] == "tool" else "secondary",
#         ):
#             st.session_state["current_page"] = "tool"
#             st.rerun()

def navbar():
    """Top navigation bar."""

    # Read current page from URL
    page = st.query_params.get("page", "about")
    st.session_state["current_page"] = page

    logo, home, tool, blank = st.columns([1.5, 0.8, 0.8, 0.1])

    with logo:
        render_html('<div class="avi-logo">AgriVision AI</div>')

    with home:
        if st.button(
            "Home",
            key="home_nav",
            use_container_width=True,
            type="primary" if page == "about" else "secondary",
        ):
            st.query_params["page"] = "about"
            st.rerun()

    with tool:
        if st.button(
            "Crop Disease Detection & Yield Prediction",
            key="tool_nav",
            use_container_width=True,
            type="primary" if page == "tool" else "secondary",
        ):
            st.query_params["page"] = "tool"
            st.rerun()
            
# def about_hero(title, subtitle):
#     """Hero section used on the About page."""

#     has_image = os.path.exists(config.HERO_IMAGE_PATH)

   

#     if has_image:
#         left, right = st.columns([2, 1])
#     else:
#         left = st.container()
#         right = None

#     with left:
#         render_html(f'<div class="hero-title">{title}</div>')
#         render_html(f'<div class="hero-subtitle">{subtitle}</div>')

#         render_html(
#             """
#             <div class="avi-chip-row">
#                 <div class="avi-chip">Unified AI System</div>
#                 <div class="avi-chip">Multimodal Learning</div>
#                 <div class="avi-chip">Explainable Predictions</div>
#                 <div class="avi-chip">Decision Support</div>
#             </div>
#             """
#         )

#         st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

#         spacer1, center, spacer2 = st.columns([1.5, 1, 1.5])

#         with center:
#             if st.button(
#                 "Try AgriVision AI",
#                 key="hero_button",
#                 type="primary",
#                 use_container_width=True,
#             ):
#                 st.session_state["current_page"] = "tool"
#                 st.rerun()

#     if right:
#         with right:
#             st.image(config.HERO_IMAGE_PATH, use_container_width=True)

#     render_html("</div>")

# def about_hero(title, subtitle):
#     """Hero section used on the About page."""

#     st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

#     has_image = os.path.exists(config.HERO_IMAGE_PATH)

#     if has_image:
#         left, right = st.columns([1.7, 1.3], gap="large")
#     else:
#         left = st.container()
#         right = None

#     with left:

#         render_html(
#             f"""
#             <h1 style="
#                 color:#1B5E20;
#                 font-size:3rem;
#                 font-weight:800;
#                 line-height:1.05;
#                 margin:0 0 35px 0;
#             ">
#                 {title}
#             </h1>
#             """
#         )

#         render_html(
#             f"""
#             <p style="
#                 font-size:1.3rem;
#                 line-height:2;
#                 color:#555;
#                 margin-bottom:45px;
#                 max-width:1100px;
#             ">
#                 {subtitle}
#             </p>
#             """
#         )

#         render_html(
#             """
#             <div style="
#                 display:flex;
#                 flex-wrap:wrap;
#                 gap:22px;
#                 margin-bottom:55px;
#             ">

#                 <div class="avi-chip">Unified AI System</div>

#                 <div class="avi-chip">Multimodal Learning</div>

#                 <div class="avi-chip">Explainable Predictions</div>

#                 <div class="avi-chip">Decision Support</div>

#             </div>
#             """
#         )

#         st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

#         left_space, center, right_space = st.columns([1, 1.2, 1])

#         with center:
#             if st.button(
#                 "Try AgriVision AI",
#                 key="hero_button",
#                 type="primary",
#                 use_container_width=True,
#             ):
#                 st.session_state["current_page"] = "tool"
#                 st.rerun()

#     if right:
#         with right:
#             st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

#             st.image(
#                 config.HERO_IMAGE_PATH,
#                 width=700,
#             )
 
def about_hero(title, subtitle):
    """Hero section used on the About page."""

    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    has_image = os.path.exists(config.HERO_IMAGE_PATH)

    if has_image:
        left, right = st.columns([1.7, 1.3], gap="large")
    else:
        left = st.container()
        right = None

    with left:

        render_html(
            f"""
            <h1 style="
                color:#1B5E20;
                font-size:3rem;
                font-weight:800;
                line-height:1.05;
                margin:0 0 35px 0;
            ">
                {title}
            </h1>
            """
        )

        render_html(
            f"""
            <p style="
                font-size:1.3rem;
                line-height:2;
                color:#555;
                margin-bottom:45px;
                max-width:1100px;
            ">
                {subtitle}
            </p>
            """
        )

        render_html(
            """
            <div style="
                display:flex;
                flex-wrap:wrap;
                gap:22px;
                margin-bottom:55px;
            ">

                <div class="avi-chip">Unified AI System</div>

                <div class="avi-chip">Multimodal Learning</div>

                <div class="avi-chip">Explainable Predictions</div>

                <div class="avi-chip">Decision Support</div>

            </div>
            """
        )

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        left_space, center, right_space = st.columns([1, 1.2, 1])

        with center:
            if st.button(
                "Try AgriVision AI",
                key="hero_button",
                type="primary",
                use_container_width=True,
            ):
                # Navigate to Tool page
                st.query_params["page"] = "tool"
                st.rerun()

    if right:
        with right:
            st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

            st.image(
                config.HERO_IMAGE_PATH,
                width=700,
            )
                               
def hero():
    """Simple static hero used on the tool page."""

    render_html(
    """
    <div class="avi-tool-hero">

        <div class="hero-title" style="
            margin-bottom:10px;
        ">
            Crop Disease Detection &amp; Yield Prediction
        </div>

        <div class="hero-subtitle" style="
            white-space: nowrap;
            font-size:1.2rem;
            margin-top:0;
        ">
            Upload a crop leaf image and provide agricultural conditions to detect diseases, estimate disease severity, predict crop yield, and understand every prediction using Explainable AI.
        </div>

    </div>
    """
)
    
    
STEP_LABELS = [
    "Upload",
    "Analyze",
    "Results",
    "Report",
]

# def step_indicator(current_step=None):
#     """current_step is accepted but unused here — kept only so the
#     existing call site in unified_page.py (theme.step_indicator(_current_step()))
#     doesn't crash with a TypeError now that this renders a plain
#     numbered stepper instead of an active/done state per step."""

#     items = ""

#     for i, label in enumerate(STEP_LABELS, start=1):
#         items += f"""
#         <div class="avi-step">
#             <span class="avi-step-number">{i}</span>
#             <span>{label}</span>
#         </div>
#         """

#         if i < len(STEP_LABELS):
#             items += (
#                 '<div style="display:flex;align-items:center;'
#                 'color:#c2c2c2;font-size:1.6rem;">&#8594;</div>'
#             )

#     render_html(
#         f'<div class="avi-steps" style="gap:10px;align-items:center;">{items}</div>'
#     )

def step_indicator(current_step=None):
    """
    Modern pill-style static step indicator.
    """

    render_html(
        """
        <style>

        .avi-stepper{
            width:100%;
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin:10px 0 45px;
            gap:18px;
        }

        .avi-step-item{
            flex:1;
            display:flex;
            align-items:center;
        }

        .avi-step-pill{

            width:100%;

    background:#ffffff;

    border:none;

    border-radius:40px;

    padding:16px 22px;

    text-align:center;

    font-size:20px;

    font-weight:700;

    color:#2E7D32;

    box-shadow:0 4px 10px rgba(0,0,0,.08);

        }



        .avi-arrow{

            font-size:28px;

            font-weight:700;

            color:#43A047;

            margin:0 12px;

            user-select:none;

        }

        @media (max-width:900px){

            .avi-stepper{

                flex-direction:column;

                align-items:stretch;

                gap:15px;

            }

            .avi-step-item{

                width:100%;

            }

            .avi-arrow{

                display:none;

            }

            .avi-step-pill{

                width:100%;

            }

        }

        </style>

        <div class="avi-stepper">

            <div class="avi-step-item">
                <div class="avi-step-pill">1. Upload</div>
            </div>

            <div class="avi-arrow">➜</div>

            <div class="avi-step-item">
                <div class="avi-step-pill">2. Analyze</div>
            </div>

            <div class="avi-arrow">➜</div>

            <div class="avi-step-item">
                <div class="avi-step-pill">3. Results</div>
            </div>

            <div class="avi-arrow">➜</div>

            <div class="avi-step-item">
                <div class="avi-step-pill">4. Report</div>
            </div>

        </div>
        """
    )
    
def severity_card(label, value, sub, level):
    """Colored severity card used to show disease severity / risk level.
    level should be one of: "green", "yellow", "red"."""

    icons = {"green": "🟢", "yellow": "🟡", "red": "🔴"}

    render_html(
        f"""
        <div class="avi-card avi-card-{level}">
        <div class="avi-card-label">{icons.get(level, "")} {label}</div>
        <div class="avi-card-value">{value}</div>
        <div class="avi-card-sub">{sub}</div>
        </div>
        """
    )