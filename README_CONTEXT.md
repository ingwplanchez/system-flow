# Contexto del Proyecto: SystemFlow Dashboard

## 1. Descripción General
SystemFlow es un Dashboard de productividad y analítica de rendimiento personal enfocado en la ingeniería de datos y la optimización del enfoque. Está diseñado bajo principios avanzados de metodologías de productividad (como la matriz de Eisenhower y bloques de tiempo de deep work) y actúa como la capa de interfaz gráfica (Frontend) de un ecosistema que posteriormente se integrará con un backend robusto en FastAPI y flujos de automatización en n8n/Make.

## 2. Objetivo de la Aplicación
El objetivo principal de SystemFlow es capturar, centralizar y transformar los registros de bloques de trabajo asignados a proyectos específicos. La aplicación expone los datos de dos formas:
* **Vista de Usuario (UI/UX):** Indicadores clave de rendimiento (KPIs) estilizados y gráficos de tendencias temporales para el análisis continuo de hábitos de enfoque.
* **Vista de Ingeniería de Datos (Pipeline ETL):** Un motor de preprocesamiento que limpia, normaliza y formatea estrictamente los datos recolectados para ser consumidos de manera directa y transparente por un motor ETL externo sin generar errores de esquema (*schema mismatch*).

## 3. Estado Actual y Objetivos Alcanzados
El prototipo frontend está construido funcionalmente en **Streamlit** utilizando `st.session_state` para simular la persistencia de datos en memoria. Se han implementado con éxito las siguientes características:
* **UI Premium y Custom CSS:** Layout oscuro moderno con componentes métricos (`st.metric`) modificados mediante CSS inyectado para mostrar valores destacados en verde neón (`#00FFA3`) y contenedores estilizados.
* **Gestión Dinámica de Proyectos:** Capacidad de registrar proyectos en tiempo real desde la barra lateral, expandiendo la lista de opciones de forma reactiva.
* **Formulario de Registro de Tareas:** Captura de bloques de trabajo asociados a proyectos específicos con campos detallados: ID de tarea, descripción de módulo, categoría, prioridad, estimación, duración real, dificultad y estado final.
* **Sincronización Cronológica Homogénea:** El campo `timestamp` se genera automáticamente en formato estricto `YYYY-MM-DD HH:MM` para mitigar excepciones de parsing.
* **Pestaña de Tendencias Temporales (Gráficos Dinámicos):** Análisis visual interactivo mediante `st.bar_chart` y `st.line_chart` mapeando las horas invertidas y la complejidad promedio distribuidas por el día de la semana (`.dt.day_name()`) de forma resiliente usando `errors='coerce'`.
* **Vista Simplificada del Historial:** Tabla interactiva para el usuario final con columnas personalizadas y renombradas (`ID`, `Fecha`, `Proyecto`, `Módulo / Tarea`, `Duración`, `Resultado`), ocultando los índices nativos de Pandas.
* **Motor de Limpieza y Exportación ETL Estricto:** Pestaña dedicada que procesa el DataFrame maestro mediante Pandas aplicando reglas de negocio automatizadas:
  - Filtrado riguroso a un esquema fijo de 9 columnas (`timestamp,task_id,project,category,priority,est_hours,real_hours,difficulty,status`), omitiendo columnas auxiliares de la interfaz (como la descripción del módulo) para blindar la ingesta del motor ETL.
  - Normalización de texto aplicando `.str.lower().str.strip()` en las columnas categóricas.
  - Truncado numérico usando `.clip(lower=0.0)` para neutralizar horas negativas accidentalmente ingresadas.
  - Acotado de rangos forzando la dificultad al intervalo cerrado de `1-5`.
  - Descarga directa en memoria (`io.StringIO`) a formato `.csv`.

