from sqlalchemy.orm import Session
from .models import Document
from .schemas import DocumentCreate

def create_document(db: Session, document_data: DocumentCreate):
    """
    Create a new document record in the database.
    """
    document = Document(
        filename=document_data.filename, 
        upload_date=document_data.upload_date, 
        text_content=document_data.text_content
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def get_document(db: Session, document_id: int):
    """
    Retrieve a document record from the database by its ID.
    """
    return db.query(Document).filter(Document.id == document_id).first()
