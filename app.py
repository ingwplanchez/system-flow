import streamlit as st
from core.state import init_session_state
from ui.styles import get_styles
from ui.layout import render_sidebar, render_dashboard

# 1. Configuración de la página
st.set_page_config(
    page_title="SystemFlow | Productivity Dashboard",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Aplicar Estilos Visuales
st.markdown(get_styles(), unsafe_allow_html=True)

# 3. Inicializar Estado de la Sesión
init_session_state()

# 4. Ejecutar Interfaz
proyecto_seleccionado = render_sidebar()
render_dashboard(proyecto_seleccionado)
