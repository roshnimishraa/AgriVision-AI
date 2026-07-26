"""
Shared helper for rendering raw HTML snippets.

Centralizing this in one place does two things:
1. Reusability — every component calls the same one-line helper instead
   of repeating `st.markdown(..., unsafe_allow_html=True)`.
2. Safety — it strips leading whitespace from every line before
   rendering. Markdown treats a line indented 4+ spaces more than its
   surroundings (after a blank line) as a literal code block, which is
   exactly what caused the tool-page hero to render as raw "<div>" text
   instead of an actual styled card. Stripping indentation here means
   no component can accidentally reintroduce that bug.
"""

import streamlit as st


def render_html(html: str):
    """Render a raw HTML snippet, safely flattened to avoid Markdown's
    indented-code-block trap."""

    flattened = "\n".join(line.strip() for line in html.strip().splitlines())
    st.markdown(flattened, unsafe_allow_html=True)
