def get_styles():
    return """
        <style>
            div[data-testid="stMetricValue"] {
                font-size: 2.2rem;
                font-weight: 700;
                color: #00FFA3;
            }
            div[data-testid="metric-container"] {
                background-color: #1E293B;
                padding: 15px;
                border-radius: 10px;
                border: 1px solid #334155;
            }
            div.stButton > button[kind="primary"] {
                background-color: #00FFA3 !important;
                color: #000000 !important;
                border: none !important;
                font-weight: 600 !important;
            }
            div.stButton > button[kind="primary"]:hover {
                background-color: #00CC82 !important;
                color: #000000 !important;
            }
            div[data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
                background-color: #FF4B4B !important;
                color: white !important;
                border: none !important;
                font-weight: 600 !important;
            }
            div[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
                background-color: #D32F2F !important;
                color: white !important;
            }
            .main .block-container {
                padding-top: 2rem;
            }
        </style>
    """
