# Named Entity Recognition API with FastAPI

This project sets up a RESTful API using FastAPI for Named Entity Recognition (NER). It includes functionality to recognize entities in provided text and to process uploaded .txt files for entity extraction.

## Project Structure

The project structure is organized as follows:

- `main.py`: Entry point for the FastAPI application.
- `requirements.txt`: Contains the necessary Python dependencies.
- `app/`:
  - `__init__.py`: Marks the directory as a Python package.
  - `api/`:
    - `endpoints.py`: Defines API endpoints for NER functionality.
    - `models.py`: Contains Pydantic models for API requests and responses.
  - `services/`:
    - `ner_service.py`: Implements Named Entity Recognition services.
    - `file_service.py`: Manages file-related operations.

## Getting Started

### Installation

1. Install dependencies:
   
   pip install -r requirements.txt
   
2. Run the FastAPI application using:

   uvicorn main:app --reload
   This command will start the FastAPI server, and you can access the API at http://127.0.0.1:8000.
