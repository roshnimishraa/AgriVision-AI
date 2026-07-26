"""
Global CSS and page config for AgriVision AI.

Every selector is grouped and commented so a specific rule is easy to
find and change without reading the whole file. This is the ONLY place
raw CSS should live — components.py should only ever reference class
names defined here, never inline styles.
"""

import streamlit as st

# ------------------------------------------------------------------
# Design tokens — change a color/radius here and it updates everywhere
# that references it below.
# ------------------------------------------------------------------
COLOR_PRIMARY = "#2e7d32"
COLOR_PRIMARY_DARK = "#256728"
COLOR_PRIMARY_DEEP = "#1b5e20"
COLOR_BORDER = "#edf1ed"
COLOR_TEXT_MUTED = "#666"
RADIUS_LG = "18px"
RADIUS_XL = "24px"

CSS = f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html,
body,
[class*="css"]{{
    font-family:'Inter',sans-serif;
}}

/* ------------------------------------------------ */
/* Hide Streamlit default UI */
/* ------------------------------------------------ */

#MainMenu{{ visibility:hidden; }}
footer{{ visibility:hidden; }}
header{{ visibility:hidden; }}

/* ------------------------------------------------ */
/* Main Page */
/* ------------------------------------------------ */

/*
.block-container{{
    max-width:1450px;
    margin-left:0;
    padding-top:1.4rem;
    padding-left:0;
    padding-right:2rem;
    padding-bottom:2rem;
}}*/

.block-container{{
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    max-width: 100% !important;

}}


/* Background */

.stApp{{
    background: linear-gradient(180deg, #fafdfb 0%, #f6faf6 45%, #ffffff 100%);
}}

/* ------------------------------------------------ */
/* Headings */
/* ------------------------------------------------ */

h1{{ font-size:2.7rem; font-weight:800; color:{COLOR_PRIMARY_DEEP}; }}
h2{{ font-size:2rem; font-weight:700; color:{COLOR_PRIMARY_DEEP}; margin-top:0.5rem; }}
h3{{ font-size:1.4rem; font-weight:700; color:{COLOR_PRIMARY}; }}
p{{ font-size:1rem; line-height:1.8; }}

/* ------------------------------------------------ */
/* Navbar */
/* ------------------------------------------------ */

.avi-navbar{{
    background:white;
    border-radius:{RADIUS_LG};
    padding:16px 22px;
    box-shadow:0 10px 30px rgba(0,0,0,.06);
    margin-bottom:25px;
    border:1px solid {COLOR_BORDER};
}}

.avi-logo{{ font-size:1.6rem; font-weight:800; color:{COLOR_PRIMARY}; }}

/* ------------------------------------------------ */
/* Hero (shared text styles — used by both the About */
/* page hero and the simple tool-page hero) */
/* ------------------------------------------------ */

.hero-badge{{
    display:inline-block;
    padding:8px 18px;
    background:#E8F5E9;
    color:{COLOR_PRIMARY};
    border-radius:999px;
    font-size:.9rem;
    font-weight:700;
    margin-bottom:18px;
}}

 /* .hero-title{{
    font-size:3rem;
    font-weight:800;
    color:{COLOR_PRIMARY_DEEP};
    line-height:1.15;
    margin-bottom:20px;
}} */

.hero-title{{
    font-size:2rem;
    font-weight:800;
    line-height:1.05;
    margin-bottom:35px;
}}

# .hero-subtitle{{
#     font-size:1.08rem;
#     line-height:2;
#     color:#555;
#     margin-bottom:28px;
# }}

.hero-subtitle{{
    font-size:1.7rem;
    line-height:2.1;
    max-width:1000px;
    color:#555;
}}

.hero-card{{
    background: linear-gradient(135deg, #f7fcf7, #eef9ef);
    border-radius:{RADIUS_XL};
    padding:45px;
    margin-bottom:35px;
    border:1px solid #e5efe5;
    box-shadow:0 15px 40px rgba(0,0,0,.05);
    transition:.3s;
}}

.hero-card:hover{{
    transform:translateY(-4px);
    box-shadow:0 18px 45px rgba(0,0,0,.08);
}}

/* Tool-page hero card — identical to .hero-card, but with an
invisible border instead of a visible outline. Kept as its own class
so the About page hero is never affected by tool-page changes. */

.avi-tool-hero{{
    /* background: linear-gradient(135deg, #f7fcf7, #eef9ef);
    
     border:1px solid transparent;
    box-shadow:0 10px 20px rgba(0,0,0,.05);
    transition:.3s; */
    border-radius:{RADIUS_XL};
    padding:15px;
    margin-bottom:10px;
    margin-top:10px;
   
}}

# .avi-tool-hero:hover{{
#     transform:translateY(-4px);
#     box-shadow:0 18px 45px rgba(0,0,0,.08);
# }}

/* ------------------------------------------------ */
/* Containers (intentionally unstyled — no boxes) */
/* ------------------------------------------------ */

div[data-testid="stVerticalBlockBorderWrapper"]{{
    border:none;
    border-radius:0;
    padding:0;
    background:transparent;
    box-shadow:none;
}}

/* ------------------------------------------------ */
/* Forms — no visible border/box around st.form(...) */
/* ------------------------------------------------ */

div[data-testid="stForm"]{{
    border:none;
    padding:0;
    background:transparent;
}}

/* ------------------------------------------------ */
/* Metrics */
/* ------------------------------------------------ */

div[data-testid="stMetric"]{{
    background:white;
    border-radius:{RADIUS_LG};
    padding:20px;
    border:1px solid {COLOR_BORDER};
    box-shadow:0 5px 15px rgba(0,0,0,.04);
}}

/* ------------------------------------------------ */
/* Buttons — primary (filled) vs secondary (outlined). */
/* Streamlit sets kind="primary"/"secondary" on the <button> itself */
/* based on the type= you pass to st.button()/st.form_submit_button(). */
/* Forcing every button to look the same green regardless of kind is */
/* what made the active/inactive navbar buttons indistinguishable. */
/* ------------------------------------------------ */

.stButton>button[kind="primary"],
.stFormSubmitButton>button[kind="primary"],
.stDownloadButton>button[kind="primary"],
.stDownloadButton>button{{
    background:{COLOR_PRIMARY};
    color:white;
    border:1px solid {COLOR_PRIMARY};
    border-radius:14px;
    font-weight:700;
    padding:12px 20px;
    transition:.3s;
}}

.stButton>button[kind="primary"]:hover,
.stFormSubmitButton>button[kind="primary"]:hover,
.stDownloadButton>button[kind="primary"]:hover,
.stDownloadButton>button:hover{{
    background:{COLOR_PRIMARY_DARK};
    color:white;
    border-color:{COLOR_PRIMARY_DARK};
    transform:translateY(-2px);
}}

.stButton>button[kind="secondary"],
.stFormSubmitButton>button[kind="secondary"]{{
    background:white;
    color:{COLOR_PRIMARY};
    border:1px solid {COLOR_PRIMARY};
    border-radius:14px;
    font-weight:700;
    padding:12px 20px;
    transition:.3s;
}}

.stButton>button[kind="secondary"]:hover,
.stFormSubmitButton>button[kind="secondary"]:hover{{
    background:#E8F5E9;
    color:{COLOR_PRIMARY_DARK};
    border-color:{COLOR_PRIMARY_DARK};
    transform:translateY(-2px);
}}

/* ------------------------------------------------ */
/* Tabs */
/* ------------------------------------------------ */

.stTabs [data-baseweb="tab"]{{ font-weight:700; font-size:1rem; }}

/* ------------------------------------------------ */
/* Cards */
/* ------------------------------------------------ */

.avi-card{{
    background:white;
    padding:22px;
    border-radius:{RADIUS_LG};
    border:1px solid {COLOR_BORDER};
    box-shadow:0 6px 20px rgba(0,0,0,.05);
    margin-bottom:16px;
    transition:.3s;
}}

.avi-card:hover{{ transform:translateY(-4px); }}

.avi-card-label{{ font-size:.95rem; font-weight:600; color:{COLOR_TEXT_MUTED}; }}
.avi-card-value{{ font-size:2rem; font-weight:800; margin-top:8px; color:{COLOR_PRIMARY_DEEP}; }}
.avi-card-sub{{ margin-top:10px; color:{COLOR_TEXT_MUTED}; line-height:1.6; }}

/* ------------------------------------------------ */
/* Severity */
/* ------------------------------------------------ */

.avi-card-green{{ border-left:7px solid {COLOR_PRIMARY}; }}
.avi-card-yellow{{ border-left:7px solid #f9a825; }}
.avi-card-red{{ border-left:7px solid #d32f2f; }}

/* ------------------------------------------------ */

img{{ border-radius:{RADIUS_LG}; }}
hr{{ margin-top:35px; margin-bottom:35px; }}

/* ------------------------------------------------ */

@media(max-width:768px){{
    .hero-card,
    .avi-tool-hero{{ padding:30px; }}
    .hero-title{{ font-size:2.2rem; }}
}}

/* ------------------------------------------------ */
/* Steps */
/* ------------------------------------------------ */

.avi-steps{{ display:flex; gap:14px; margin-bottom:30px; flex-wrap:wrap; }}

.avi-step{{
    background:white;
    border-radius:14px;
    padding:18px;
    font-weight:700;
    transition:.3s;
    border:1px solid #ECECEC;
    box-shadow:0 5px 15px rgba(0,0,0,.05);
    color:#999;
}}

.avi-step:hover{{ transform:translateY(-4px); }}

.avi-step.active{{
    background:white;
    color:#1B5E20;
    border-color:{COLOR_PRIMARY};
    box-shadow:0 6px 18px rgba(46,125,50,.15);
}}

.avi-step.done{{
    background:white;
    color:{COLOR_PRIMARY};
    border-color:#81C784;
}}

/* ------------------------------------------------ */
/* Chip row (grouped highlights, no individual box shadows) */
/* ------------------------------------------------ */

.avi-chip-row{{
    display:flex;
    flex-wrap:wrap;
    gap:18px;
    margin:45px 0;
}}

.avi-chip{{
    background:#F3F8F3;
    color:#1B5E20;
    margin-top: -15px;
    padding:15px 18px;
    border-radius:999px;
    font-size:1rem;
    font-weight:700;
}}

.avi-chip-icon{{ font-size:1.3rem; }}

.stFileUploader{{
    background:white;
    border-radius:{RADIUS_LG};
    padding:15px;
    border:1px solid #ECECEC;
}}

div[data-testid="stImage"] img{{
    border-radius:{RADIUS_LG};
    box-shadow:0 10px 30px rgba(0,0,0,.08);
}}

/* ------------------------------------------------ */
/* Hero stats (About page) */
/* ------------------------------------------------ */

.hero-stats{{ display:flex; gap:18px; margin-top:25px; flex-wrap:wrap; }}

.hero-stat{{
    background:white;
    border-radius:14px;
    border:1px solid #ECECEC;
    padding:18px;
    min-width:150px;
    text-align:center;
    box-shadow:0 4px 15px rgba(0,0,0,.05);
}}

.hero-number{{ font-size:1.8rem; color:{COLOR_PRIMARY}; font-weight:800; }}
.hero-label{{ color:{COLOR_TEXT_MUTED}; font-size:.95rem; }}

/* ------------------------------------------------ */
/* Model Validation Cards */
/* ------------------------------------------------ */

.avi-figure-card{{

    background:#ffffff;

    border:1px solid #E8ECEF;

    border-radius:20px;

    padding:22px;

    margin-bottom:24px;

    box-shadow:0 6px 18px rgba(0,0,0,.06);

    overflow:hidden;
}}

.avi-fig-title{{

    font-size:1.35rem;

    font-weight:800;

    color:#1B5E20;

    text-align:center;

    margin-bottom:18px;

    line-height:1.4;
}}

.avi-fig-caption {{

    margin-top:18px;

    font-size:1rem;

    line-height:1.8;

    color:#555;

    text-align:center;
}}

/* Validation Images */

.avi-figure-card img{{

    width:100%;

    border-radius:16px !important;

    border:none !important;

    box-shadow:none !important;

    margin-bottom:12px;
}}


</style>
"""


def apply():
    """Sets the page config and injects the global stylesheet. Call
    this once, at the very top of the app entry point."""

    st.set_page_config(
        page_title="AgriVision AI",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown(CSS, unsafe_allow_html=True)