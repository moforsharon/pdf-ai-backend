import os
from datetime import datetime
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..pdf_processing import extract_text_from_pdf
from ..crud import create_document
from ..schemas import DocumentCreate

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/documents/")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Endpoint to upload a document, extract text from the PDF, and store it in the database.
    """
    file_location = f"files/{file.filename}"
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    
    # Save the uploaded file
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    try:
        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(file_location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Create document data schema
    document_data = DocumentCreate(filename=file.filename, upload_date=datetime.now(), text_content=text)
    
    # Save the document data to the database
    document = create_document(db, document_data)
    
    return {"filename": document.filename, "id": document.id, "text": text}
