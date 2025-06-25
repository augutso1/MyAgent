# MyAgent

Your own AI Agent to talk with your documents.

## Overview

MyAgent is a RAG (Retrieval-Augmented Generation) system that allows you to upload PDF documents and interact with them using natural language queries. The system uses Google's Gemini AI model for generating responses and ChromaDB for vector storage.

## Features

- PDF document upload and processing
- Text extraction and chunking
- Vector-based document retrieval
- AI-powered question answering using Gemini
- RESTful API interface

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini AI
- Virtual environment (recommended)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd MyAgent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

4. Install additional required packages:

```bash
pip install langchain chromadb sentence-transformers pypdf python-dotenv
```

5. Create a `.env` file in the backend directory:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the Application

1. Navigate to the backend directory:

```bash
cd backend
```

2. Start the FastAPI server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Health Check

- **GET** `/api/v1/health`
- Returns the API status

### Upload Document

- **POST** `/api/v1/upload`
- Upload a PDF file for processing and indexing
- Content-Type: `multipart/form-data`
- Body: `file` (PDF file)

### Chat Query

- **POST** `/api/v1/chat`
- Ask questions about uploaded documents
- Content-Type: `application/json`
- Body: `{"question": "your question here"}`

### Query (Alternative)

- **POST** `/api/v1/query`
- Alternative endpoint for asking questions
- Same format as chat endpoint

## Testing the API

### 1. Health Check

```bash
curl -X GET "http://localhost:8000/api/v1/health"
```

Expected response:

```json
{ "status": "ok" }
```

### 2. Upload a PDF Document

```bash
curl -X POST "http://localhost:8000/api/v1/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/document.pdf"
```

Expected response:

```json
{
  "filename": "document.pdf",
  "message": "Arquivo recebido e enviado para processamento."
}
```

### 3. Ask Questions

```bash
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic of the document?"}'
```

Expected response:

```json
{
  "answer": "The document discusses...",
  "source_found": true
}
```

## Using Python Requests

```python
import requests

# Upload a document
with open('document.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/api/v1/upload', files=files)
    print(response.json())

# Ask a question
question_data = {"question": "What are the key points in the document?"}
response = requests.post('http://localhost:8000/api/v1/chat', json=question_data)
print(response.json())
```

## Project Structure

```
MyAgent/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py          # API endpoints
│   │   ├── core/
│   │   │   └── config.py          # Configuration
│   │   ├── schemas/
│   │   │   └── chat.py            # Pydantic models
│   │   ├── services/
│   │   │   └── rag_service.py     # RAG implementation
│   │   ├── storage/
│   │   │   └── vector_store.py    # Vector database
│   │   └── main.py                # FastAPI application
│   ├── data/                      # Uploaded documents
│   ├── chroma_db/                 # Vector database storage
│   └── requirements.txt           # Python dependencies
└── README.md
```

## Configuration

The application uses the following configuration:

- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters
- **Retrieval Results**: 3 most relevant chunks
- **AI Model**: Gemini 2.0 Flash

## Troubleshooting

1. **Google API Key Error**: Ensure your `.env` file contains a valid `GOOGLE_API_KEY`
2. **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port in the uvicorn command or kill the process using the port
4. **PDF Processing Errors**: Ensure the PDF file is not corrupted and is readable

## License

This project is licensed under the MIT License.
