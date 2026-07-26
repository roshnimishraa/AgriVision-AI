import streamlit as st

from src.ui import theme, about_page, unified_page

theme.apply()
theme.navbar()

if st.session_state.get("current_page") == "about":
    about_page.render()
else:
    unified_page.render()
