# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands
- **Run Frontend**: `streamlit run frontend/app.py`
- **Run Backend**: `uvicorn backend.main:app --reload` (assuming `backend/main.py` as entry point)
- **Infrastructure**: `docker-compose up` to launch the full stack (FastAPI + Streamlit)

## Architecture & Structure
The project follows a decoupled three-layer architecture:
1. **Frontend (`frontend/`)**: Streamlit-based dashboard. Handles UI, user interaction, and data visualization. Currently uses `st.session_state` for simulation, moving towards an API-driven state.
2. **Backend (`backend/`)**: FastAPI REST API. Responsible for relational persistence via SQLAlchemy/SQLite and Pydantic validation.
3. **Analytics Engine (`data_analysis/`)**: Isolated logic for computing productivity metrics (e.g., "Focus Score") using Pandas for temporal aggregations.

## Key Technical Constraints
- **Data Ingestion**: Any CSV ingestion or data export MUST strictly adhere to the specifications in [DATA_SCHEMA.md](DATA_SCHEMA.md). 
    - Mandatory 9 columns: `timestamp`, `task_id`, `project`, `category`, `priority`, `est_hours`, `real_hours`, `difficulty`, `status`.
    - Strict normalization: Categorical strings must be lowercase and stripped.
    - Value clamping: `difficulty` must be between 1-5; hours must be $\ge 0$.
- **Modularity**: The system is designed for low coupling. The frontend should interact with the backend via HTTP requests, never directly accessing the database.
