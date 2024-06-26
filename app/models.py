from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Document(Base):
    """
    ORM model for the 'documents' table.
    """
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    filename = Column(String, index=True)  # Column to store the filename
    upload_date = Column(String)  # Column to store the upload date
    text_content = Column(Text)  # Column to store the extracted text content from the document
