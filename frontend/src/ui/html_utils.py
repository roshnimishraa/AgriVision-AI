import streamlit as st


def render_html(html: str):

    flattened = "\n".join(line.strip() for line in html.strip().splitlines())
    st.markdown(flattened, unsafe_allow_html=True)