from io import StringIO
import csv
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities_from_text(text):
    processed_text = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in processed_text.ents]
    return entities

def generate_csv(entities):
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerow(["Text", "Entity"])

    for entity in entities:
        csv_writer.writerow([entity["text"], entity["label"]])

    return csv_data.getvalue()
