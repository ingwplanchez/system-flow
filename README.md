# SystemFlow ⚙️

**SystemFlow** es una plataforma de análisis de productividad diseñada para medir y optimizar el tiempo de trabajo profundo (*deep work*). El sistema registra sesiones de trabajo, calcula métricas de enfoque mediante lógica de negocio personalizada y visualiza tendencias mediante análisis de datos en tiempo real.

## Stack Tecnológico
* **Backend:** FastAPI (Python) para la gestión de APIs y persistencia de datos.
* **Frontend:** Streamlit para la visualización de datos y el dashboard interactivo.
* **Data Science:** Pandas para el procesamiento, limpieza y análisis de tendencias de productividad.
* **Base de Datos:** SQLite (para despliegue local sencillo).

---

## 🚀 Siguientes Pasos Técnicos
Para mantener el *momentum* y asegurar una arquitectura escalable, dividiremos el desarrollo en los siguientes sprints:

### Sprint 1: Backend
* Creación de los modelos de datos (`models.py`) para las entidades de `Proyectos` y `Tareas`.
* Implementación de los endpoints principales en FastAPI (ej: `POST /proyectos/`, `POST /tareas/`).

### Sprint 2: Data & Logic
* Desarrollo de `metrics.py`: Script de procesamiento que importe los datos y calcule la "Puntuación de Enfoque" basándose en tu lógica de negocio (sesiones completadas vs. tiempo real vs. dificultad).

### Sprint 3: Integración Frontend
* Conexión del dashboard de Streamlit con la API de FastAPI mediante `requests` o `httpx`.
* Migración de `st.session_state` a persistencia real mediante peticiones HTTP.

---

## 🛠️ ¿Cómo quieres continuar?

Podemos tomar dos caminos para avanzar ahora mismo:

* **[Opción A] Backend:** Empezamos a redactar la estructura del proyecto en FastAPI y definimos los modelos de datos para registrar las tareas y proyectos de forma persistente.
* **[Opción B] Análisis:** Definimos la lógica matemática detallada de tu "Puntuación de Enfoque" y creamos el script de Pandas para que el sistema tenga un "cerebro" analítico desde el primer día.

---
*Desarrollado por Wilmer Planchez - Ingeniero Mecatrónico | Especialista en Automatización e IA.*