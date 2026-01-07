"""
Global UI configuration for Visual AI.
Enforces design constraints before implementing Figma sections.
"""

def get_base_css() -> str:
    """
    Returns base CSS that enforces global design constraints.
    
    Constraints:
    - Light theme only
    - System font / Inter-like
    - Minimal animations (but allow icons to work)
    - Clean, minimal styling
    """
    return """
    <style>
        /* Force light theme */
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        
        /* System font stack (Inter-like) - but NOT for icons */
        body, .stMarkdown, .stText, p, span, div:not([data-testid*="stIcon"]):not(.material-icons) {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                         'Helvetica Neue', Arial, sans-serif;
        }
        
        /* Allow icons to render properly */
        [data-testid*="stIcon"], .material-icons, .material-icons-outlined {
            font-family: 'Material Icons', 'Material Icons Outlined' !important;
        }
        
        /* Reduce animations but don't remove completely (breaks icons) */
        * {
            transition-duration: 0.1s !important;
        }
        
        /* Remove shadows */
        .stButton button,
        .stTextInput input,
        .stSelectbox select {
            box-shadow: none !important;
        }
        
        /* Clean button styles */
        .stButton button {
            border-radius: 4px;
        }
        
        /* Ensure wide layout is respected */
        .main .block-container {
            max-width: 100%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        
        /* Prevent layout shift on rerun */
        .main {
            overflow-anchor: none;
        }
        
        /* Center and size images in chat interface */
        .main img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 200px !important;
            max-height: 200px !important;
            width: auto !important;
            height: auto !important;
            border-radius: 8px;
            object-fit: contain;
        }
        
        /* Force Streamlit image container to be small */
        .main [data-testid="stImage"] {
            max-width: 200px !important;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* Style the expander for image */
        .streamlit-expanderHeader {
            font-size: 14px;
            font-weight: 500;
        }
    </style>
    """


# Font size constants 
FONT_SIZES = {
    "app_title": "42px",           # Main app title
    "section_header": "18px",      # Sidebar section headers
    "chat_text": "14px",           # Chat message text
    "helper_text": "12px",         # Helper/secondary text
    "button_text": "14px",         # Button labels
}

# Color constants (light theme)
COLORS = {
    "background": "#FFFFFF",
    "text_primary": "#000000",
    "text_secondary": "#666666",
    "border": "#E0E0E0",
}
