from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    """
    Schema for creating a new document.
    """
    filename: str
    upload_date: datetime = None  # Optional upload date, defaults to None
    text_content: str

class Document(BaseModel):
    """
    Schema for reading document data, which includes the database-generated ID.
    """
    id: int
    filename: str
    upload_date: datetime
    text_content: str

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models
