from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_document
from ..nlp_processor import answer_question

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/questions/{doc_id}")
async def ask_question(doc_id: int, request: Request, db: Session = Depends(get_db)):
    """
    Endpoint to ask a question based on the content of an uploaded document.
    """
    try:
        question_data = await request.json()
        question = question_data.get("question")
        if not question:
            raise ValueError("Question field is required")

        document = get_document(db, document_id=doc_id)
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")

        answer = answer_question(document.text_content, question)
        return {"question": question, "answer": answer}
    except Exception as e:
        # Return the exception message for debugging
        return {"error": str(e)}
