"""
Facade module — kept so existing code doing `from src.ui import theme`
and calling `theme.apply()`, `theme.hero()`, etc. keeps working exactly
as before, without every page needing to change its imports.

The actual implementation now lives in:
    styles.py      -> apply() and all CSS
    components.py  -> navbar(), hero(), about_hero(), step_indicator(),
                       severity_card()
    html_utils.py  -> shared render_html() helper

If you're looking for how something is styled or rendered, go to
those files directly — this one is intentionally just re-exports.
"""

from src.ui.styles import apply
from src.ui.components import (
    navbar,
    about_hero,
    hero,
    step_indicator,
    severity_card,
)

__all__ = [
    "apply",
    "navbar",
    "about_hero",
    "hero",
    "step_indicator",
    "severity_card",
]
