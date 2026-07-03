import pandas as pd
import numpy as np

def procesar_datos_etl(df):
    df_clean = df.copy()
    columnas_estrictas = ['timestamp', 'task_id', 'project', 'category', 'priority', 'est_hours', 'real_hours', 'difficulty', 'status']
    df_clean = df_clean[[col for col in columnas_estrictas if col in df_clean.columns]]
    columnas_criticas = ['timestamp', 'task_id', 'project', 'category', 'status']
    df_clean = df_clean.dropna(subset=[col for col in columnas_criticas if col in df_clean.columns])

    # Normalización de Formato de Fecha (ISO 8601: YYYY-MM-DD HH:MM:SS)
    if 'timestamp' in df_clean.columns:
        df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')

    for col in ['category', 'priority', 'status']:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.lower().str.strip()
    if 'est_hours' in df_clean.columns: df_clean['est_hours'] = df_clean['est_hours'].clip(lower=0.0)
    if 'real_hours' in df_clean.columns: df_clean['real_hours'] = df_clean['real_hours'].clip(lower=0.0)
    if 'difficulty' in df_clean.columns: df_clean['difficulty'] = df_clean['difficulty'].clip(1, 5)
    for col in columnas_estrictas:
        if col not in df_clean.columns: df_clean[col] = np.nan
    return df_clean[columnas_estrictas]
