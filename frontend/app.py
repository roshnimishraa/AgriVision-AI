import streamlit as st

from src.ui import theme, about_page, unified_page

theme.apply()
theme.navbar()

if st.session_state.get("current_page") == "about":
    about_page.render()
else:
<<<<<<< HEAD
    unified_page.render()
=======
    unified_page.render()
>>>>>>> 8295c80c326721114d7f66a83a8961e80eb416f0
