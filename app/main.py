from fastapi import FastAPI
from app.api.endpoints import recognize_entities, upload_file

app = FastAPI()
spell = SpellChecker()
nlp = spacy.load("en_core_web_sm")
nlp_oliverguhr = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")

app.include_router(recognize_entities.router)
app.include_router(upload_file.router)
app.include_router(spelling_corrector.router)
