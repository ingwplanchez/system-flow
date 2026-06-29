import streamlit as st
import pandas as pd
import numpy as np

def init_session_state():
    if 'proyectos' not in st.session_state:
        st.session_state['proyectos'] = ["Todos los Proyectos", "Ultra Enfoque", "Nexus Flow", "Vendedor Digital"]

    if 'session_active' not in st.session_state:
        st.session_state['session_active'] = False

    if 'session_start_time' not in st.session_state:
        st.session_state['session_start_time'] = None

    if 'df_tareas' not in st.session_state:
        st.session_state['df_tareas'] = pd.DataFrame([
            {"timestamp": "2026-06-25 09:00", "task_id": "T-001", "project": "Ultra Enfoque", "module_task": "Refactorización Backend", "category": "deep_work", "priority": "high", "est_hours": 2.0, "real_hours": 0.75, "difficulty": 3, "status": "Completed"},
            {"timestamp": "2026-06-26 11:30", "task_id": "T-002", "project": "Nexus Flow", "module_task": "Diseño de PCB en KiCad", "category": "collaboration", "priority": "medium", "est_hours": 1.0, "real_hours": 0.75, "difficulty": 2, "status": "Interrupted"},
            {"timestamp": "2026-06-27 14:00", "task_id": "T-003", "project": "Vendedor Digital", "module_task": "Configuración de Webhooks n8n", "category": "strategy", "priority": "critical", "est_hours": 4.0, "real_hours": 0.5, "difficulty": 4, "status": "Completed"}
        ])
