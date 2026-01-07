"""
Global UI configuration for Visual AI.
Clean, consolidated purple theme styling.
"""

def get_base_css() -> str:
    """
    Returns consolidated base CSS for purple theme.
    Single source of truth for all styling.
    """
    return """
    <style>
        /* ===== GLOBAL THEME ===== */
        .stApp {
            background-color: #1a0b2e;
            color: #FFFFFF;
        }
        
        /* System fonts */
        body, .stMarkdown, .stText, p, span, div:not([data-testid*="stIcon"]):not(.material-icons) {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            color: #FFFFFF;
        }
        
        /* Allow icons to render */
        [data-testid*="stIcon"], .material-icons, .material-icons-outlined {
            font-family: 'Material Icons', 'Material Icons Outlined' !important;
        }
        
        /* Minimal animations */
        * {
            transition-duration: 0.1s !important;
        }
        
        /* ===== HEADER ===== */
        header[data-testid="stHeader"] {
            background-color: #1a0b2e !important;
        }
        
        .stDeployButton {
            display: none;
        }
        
        /* ===== MAIN AREA ===== */
        .main .block-container {
            max-width: 100%;
            padding: 1rem 2rem 3rem 2rem !important;
        }
        
        .main {
            overflow-anchor: none;
        }
        
        /* Images */
        .main img {
            display: block;
            margin: 0 auto;
            max-width: 200px !important;
            max-height: 200px !important;
            width: auto !important;
            height: auto !important;
            border-radius: 8px;
            object-fit: contain;
        }
        
        .main [data-testid="stImage"] {
            max-width: 200px !important;
            margin: 0 auto;
        }
        
        /* Expanders in main area */
        .main details,
        .main [data-testid="stExpander"] {
            background-color: #1a0b2e !important;
        }
        
        .main details summary,
        .main [data-testid="stExpander"] summary,
        .main .streamlit-expanderHeader {
            background-color: #3a2a5a !important;
            color: #FFFFFF !important;
            border-color: #4a3a6a !important;
        }
        
        .main .streamlit-expanderContent {
            background-color: #1a0b2e !important;
        }
        
        /* Chat input */
        .main [data-testid="stChatInput"],
        .main [data-testid="stChatInput"] > div,
        .main [data-testid="stBottom"],
        .main [data-testid="stBottom"] > div {
            background-color: #1a0b2e !important;
        }
        
        .main [data-testid="stChatInput"] textarea {
            background-color: #3a2a5a !important;
            color: #FFFFFF !important;
            border-color: #4a3a6a !important;
        }
        
        .main [data-testid="stChatInput"] textarea::placeholder {
            color: #B0B0B0 !important;
        }
        
        /* ===== SIDEBAR ===== */
        section[data-testid="stSidebar"] {
            background-color: #2a1a4a !important;
        }
        
        /* Sidebar text */
        section[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div {
            color: #FFFFFF !important;
        }
        
        /* Sidebar inputs */
        section[data-testid="stSidebar"] input,
        section[data-testid="stSidebar"] textarea {
            background-color: #3a2a5a !important;
            color: #FFFFFF !important;
            border-color: #4a3a6a !important;
        }
        
        /* Sidebar buttons */
        section[data-testid="stSidebar"] button {
            color: #FFFFFF !important;
        }
        
        section[data-testid="stSidebar"] button[kind="secondary"],
        section[data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {
            background-color: #3a2a5a !important;
            border: 1px solid #4a3a6a !important;
        }
        
        section[data-testid="stSidebar"] button[kind="secondary"]:hover,
        section[data-testid="stSidebar"] button[data-testid="baseButton-secondary"]:hover {
            background-color: #4a3a6a !important;
        }
        
        /* Sidebar expanders */
        section[data-testid="stSidebar"] details,
        section[data-testid="stSidebar"] .streamlit-expanderContent {
            background-color: #2a1a4a !important;
        }
        
        section[data-testid="stSidebar"] details summary,
        section[data-testid="stSidebar"] .streamlit-expanderHeader {
            background-color: #3a2a5a !important;
            color: #FFFFFF !important;
            border-color: #4a3a6a !important;
        }
        
        /* Sidebar file uploader */
        section[data-testid="stSidebar"] [data-testid="stFileUploader"],
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] > div,
        section[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"],
        section[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"] > div {
            background-color: #3a2a5a !important;
            border-color: #4a3a6a !important;
        }
        
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] label,
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] small {
            color: #E0E0E0 !important;
        }
        
        /* ===== UNIVERSAL OVERRIDES ===== */
        hr {
            margin: 1rem 0 1.5rem 0 !important;
        }
        
        .stButton button,
        .stTextInput input,
        .stSelectbox select {
            box-shadow: none !important;
            border-radius: 4px;
        }
    </style>
    """


# Font size constants 
FONT_SIZES = {
    "app_title": "42px",
    "section_header": "18px",
    "chat_text": "14px",
    "helper_text": "12px",
    "button_text": "14px",
}

# Color constants
COLORS = {
    "background": "#1a0b2e",
    "sidebar_bg": "#2a1a4a",
    "element_bg": "#3a2a5a",
    "border": "#4a3a6a",
    "text_primary": "#FFFFFF",
    "text_secondary": "#E0E0E0",
}
