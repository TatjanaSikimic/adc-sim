"""Sphinx configuration for ADC-Sim documentation."""

project = "ADC-Sim"
author = "Tatjana Babic"
copyright = "2026, Tatjana Babic"

extensions = ["sphinx_needs"]

exclude_patterns = ["_build"]

# --- HTML output ------------------------------------------------------------

html_theme = "furo"
html_title = "ADC-Sim"

# B612: open-source typeface designed by Airbus for cockpit displays.
html_css_files = [
    "https://fonts.googleapis.com/css2?family=B612:wght@400;700&family=B612+Mono&display=swap",
]

html_theme_options = {
    "light_css_variables": {
        "font-stack": "B612, sans-serif",
        "font-stack--monospace": "'B612 Mono', monospace",
        "color-brand-primary": "#0e7c86",
        "color-brand-content": "#0e7c86",
        "color-background-secondary": "#f2f6f8",
    },
    "dark_css_variables": {
        "color-brand-primary": "#40e0d0",
        "color-brand-content": "#40e0d0",
        "color-background-primary": "#0b1622",
        "color-background-secondary": "#101f2e",
        "color-foreground-primary": "#e6edf3",
    },
}


# --- sphinx-needs -----------------------------------------------------------

needs_types = [
    {
        "directive": "sys",
        "title": "System Requirement",
        "prefix": "SYS_ADC_",
        "color": "#BFD8D2",
        "style": "node",
    },
    {
        "directive": "srs",
        "title": "Software Requirement",
        "prefix": "SRS_ADC_",
        "color": "#FEDCD2",
        "style": "node",
    },
]

needs_extra_options = ["verification"]

needs_id_required = True
needs_id_regex = r"^(SYS|SRS)_ADC_\d{3}$"

needs_statuses = [
    {"name": "draft", "description": "Written, not yet reviewed"},
    {"name": "approved", "description": "Reviewed and accepted"},
]
