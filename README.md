# SmartSDLC – AI-Enhanced Software Development Lifecycle

This project demonstrates the integration of generative AI (IBM Watsonx / Granite) into a modern SDLC toolchain using FastAPI and Streamlit.

# Modules Covered in the Code:
The SmartSDLC will cover automation in these stages:

Requirement Analysis – Convert user stories to structured requirements.

Design Suggestion – Generate UML design ideas.

Code Generation – Auto-generate code templates.

Testing – Generate test cases based on code.

Deployment – Optional integration with CI/CD tools (can be simulated).

Documentation – Auto-generate developer/user documentation

## Project Structure

- `backend/` – FastAPI backend to handle routing and AI integration.
- `frontend/` – Streamlit frontend for user interaction.
- `models/` – AI model placeholder and Watsonx API integration hooks.

## Technologies Used

- Python
- FastAPI
- Streamlit
- IBM Watsonx AI (Granite models)

## Setup Instructions

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run backend
cd backend
uvicorn main:app --reload

# Run frontend
cd ../frontend
streamlit run app.py
```

## Milestones Implemented
1. Model Selection & Architecture
2. Core Functionalities (FastAPI)
3. Frontend (Streamlit)
4. Deployment-ready local testing
