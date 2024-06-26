
# AI-Powered Document Question Answering Backend

This repository contains the backend code for an AI-powered document question-answering system. The system allows users to upload PDF documents and ask questions about their content. The backend processes the documents, extracts text, and uses natural language processing to provide answers to the users' questions.

## Features

- **PDF Upload**: Users can upload PDF documents to the system.
- **Text Extraction**: Extract text content from uploaded PDF documents.
- **Question Answering**: Use NLP to answer questions based on the content of the uploaded documents.
- **Database Integration**: Store and retrieve document information and text content.

## Project Structure

```
ai-planet-be/
├── alembic/
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── documents.py
│   │   └── questions.py
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── nlp_processor.py
│   ├── pdf_processing.py
│   └── schemas.py
├── env/
├── migrations/
├── .env
├── alembic.ini
└── LICENSE
```

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- PyMuPDF
- LangChain
- OpenAI API Key

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AI-planet-Project/ai-planet-backend.git
cd ai-planet-backend
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project and add the following values:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your-langchain-api-key
LANGCHAIN_PROJECT=your-langchain-project
OPENAI_API_KEY=your-openai-api-key

```

### 5. Initialize the Database

Run the following command to create all database tables:

```bash
python -m app.database
```

### 6. Run the Application

Start the FastAPI application with:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Upload Document

- **URL**: `/api/documents/`
- **Method**: `POST`
- **Description**: Uploads a PDF document, extracts text content, and stores it in the database.

### 2. Ask Question

- **URL**: `/api/questions/{doc_id}`
- **Method**: `POST`
- **Description**: Asks a question based on the content of an uploaded document.

## Project Modules

### 1. `main.py`

- Initializes the FastAPI application and includes routers.

### 2. `database.py`

- Sets up the database connection and session management.
- Provides a function to create all tables.

### 3. `models.py`

- Defines the SQLAlchemy ORM model for the `Document` table.

### 4. `schemas.py`

- Defines Pydantic models for data validation and serialization.

### 5. `crud.py`

- Provides CRUD operations for interacting with the database.

### 6. `pdf_processing.py`

- Contains functions to extract text from PDF documents.

### 7. `nlp_processor.py`

- Contains functions to process questions and generate answers using LangChain.

### 8. `routers/documents.py`

- Defines the API endpoint for uploading documents.

### 9. `routers/questions.py`

- Defines the API endpoint for asking questions based on document content.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
