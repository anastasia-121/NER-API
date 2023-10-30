from fastapi import FastAPI
from app.api.endpoints import recognize_entities, upload_file

app = FastAPI()

app.include_router(recognize_entities.router)
app.include_router(upload_file.router)
