from fastapi import FastAPI
from app.routers import documents, questions 
from .database import create_all_tables
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Create all database tables
create_all_tables()

# Include routers for different endpoints
app.include_router(documents.router, prefix="/api")
app.include_router(questions.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
