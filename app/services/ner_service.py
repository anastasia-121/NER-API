from fastapi import HTTPException
from io import StringIO
import csv

from app.api.models import TextInput

async def recognize_entities(data: TextInput):
        if not data.text:
        raise HTTPException(status_code=400, detail="No text provided")

    try:
        processed_text = nlp(data.text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in processed_text.ents]

        for entity in processed_text.ents:
            print(f"Text: {entity.text}, Entity: {entity.label_}")

        return {"text": data.text, "entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing text")

async def process_uploaded_file(file):
        if file.filename.endswith(".txt"):
        try:
            contents = await file.read()
            text = contents.decode("utf-8")

            processed_text = nlp(text)
            entities = [{"text": ent.text, "label": ent.label_} for ent in processed_text.ents]

            #StringIO object to store CSV data
            csv_data = StringIO()
            csv_writer = csv.writer(csv_data)

            # make a header
            csv_writer.writerow(["Text", "Entity"])

            for entity in processed_text.ents:
                csv_writer.writerow([entity.text, entity.label_])

            # Set response headers for file download
            from starlette.responses import StreamingResponse
            response = StreamingResponse(iter([csv_data.getvalue()]), media_type="text/csv")
            response.headers["Content-Disposition"] = f"attachment; filename=extracted_entities.csv"

            return response

        except Exception as e:
            raise HTTPException(status_code=500, detail="Error processing uploaded file")
    else:
        raise HTTPException(status_code=400, detail="Only .txt files are allowed")
