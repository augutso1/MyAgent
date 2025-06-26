---
title: MyAgent
emoji: 📉
colorFrom: green
colorTo: indigo
sdk: docker
pinned: false
license: mit
short_description: Your own AI Agent to talk with your documents.
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# MyAgent

Your own AI Agent to talk with your documents.

## Overview

MyAgent is a complete RAG (Retrieval-Augmented Generation) system that allows you to upload PDF documents and interact with them using natural language queries. The system features a modern web interface built with Next.js and a robust FastAPI backend powered by Google's Gemini AI model and ChromaDB for vector storage.

## Features

- **Modern Web Interface**: Beautiful, responsive UI built with Next.js and Tailwind CSS
- **PDF Document Processing**: Upload and process PDF files with automatic text extraction
- **Intelligent Chunking**: Advanced text splitting for optimal document understanding
- **Vector-Based Retrieval**: ChromaDB-powered semantic search across documents
- **AI-Powered Q&A**: Google Gemini 2.0 Flash for intelligent responses
- **Real-time Chat**: Interactive chat interface with streaming responses
- **RESTful API**: Complete API for integration with other applications
- **Docker Support**: Containerized deployment for easy setup and scaling

## Tech Stack

### Frontend

- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **React Hooks** - State management and side effects

### Backend

- **FastAPI** - Modern Python web framework
- **Google Gemini AI** - Advanced language model
- **ChromaDB** - Vector database for embeddings
- **LangChain** - LLM application framework
- **PyPDF** - PDF text extraction
- **Sentence Transformers** - Text embeddings

## Quick Start

### Option 1: Docker (Recommended)

1. **Clone the repository**:

```bash
git clone <repository-url>
cd MyAgent
```

2. **Set up your API key**:

```bash
echo "GOOGLE_API_KEY=your_google_api_key_here" > backend/.env
```

3. **Run with Docker Compose**:

```bash
docker-compose up --build
```

4. **Access the application**:

- **Web Interface**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Backend API**: http://localhost:8000

### Option 2: Manual Setup

#### Backend Setup

1. **Create virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**:

```bash
cd backend
pip install -r requirements.txt
```

3. **Configure environment**:

```bash
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```

4. **Start the server**:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

1. **Install dependencies**:

```bash
cd frontend
npm install
```

2. **Start development server**:

```bash
npm run dev
```

3. **Access the application**: http://localhost:3000

## How to Use

### 1. Upload Documents

- Click "Selecionar Arquivo PDF" to choose a PDF file
- Click "Fazer Upload e Indexar" to process and index the document
- The system will automatically extract text, create chunks, and generate embeddings

### 2. Ask Questions

- Use the chat interface to ask questions about your uploaded documents
- The AI will search through your documents and provide relevant answers
- Questions are processed in real-time with streaming responses

### 3. API Integration

- Use the RESTful API endpoints for programmatic access
- Full API documentation available at `/docs`
- Support for both file uploads and chat queries

## API Endpoints

### Health Check

```http
GET /api/v1/health
```

### Upload Document

```http
POST /api/v1/upload
Content-Type: multipart/form-data
Body: file (PDF)
```

### Chat Query

```http
POST /api/v1/chat
Content-Type: application/json
Body: {"question": "your question here"}
```

### Alternative Query Endpoint

```http
POST /api/v1/query
Content-Type: application/json
Body: {"question": "your question here"}
```

## Testing Examples

### Using cURL

**Health Check**:

```bash
curl -X GET "http://localhost:8000/api/v1/health"
```

**Upload Document**:

```bash
curl -X POST "http://localhost:8000/api/v1/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"
```

**Ask Question**:

```bash
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic of the document?"}'
```

### Using Python

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
├── frontend/                    # Next.js web application
│   ├── app/
│   │   ├── components/         # React components
│   │   │   ├── Chat.tsx       # Chat interface
│   │   │   └── FileUpload.tsx # File upload component
│   │   ├── services/          # API services
│   │   │   └── api.ts         # API client functions
│   │   ├── globals.css        # Global styles
│   │   ├── layout.tsx         # Root layout
│   │   └── page.tsx           # Main page
│   ├── public/                # Static assets
│   ├── package.json           # Node.js dependencies
│   ├── Dockerfile             # Frontend container
│   └── next.config.ts         # Next.js configuration
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py      # API endpoints
│   │   ├── core/
│   │   │   └── config.py      # Configuration
│   │   ├── schemas/
│   │   │   └── chat.py        # Pydantic models
│   │   ├── services/
│   │   │   └── rag_service.py # RAG implementation
│   │   ├── storage/
│   │   │   └── vector_store.py # Vector database
│   │   └── main.py            # FastAPI application
│   ├── data/                  # Uploaded documents
│   ├── chroma_db/             # Vector database storage
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile             # Backend container
├── docker-compose.yml         # Multi-container orchestration
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## Configuration

### AI Model Settings

- **Model**: Gemini 2.0 Flash
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters
- **Retrieval Results**: 3 most relevant chunks

### Development Settings

- **Backend Port**: 8000
- **Frontend Port**: 3000
- **API Base URL**: http://localhost:8000/api/v1

## Docker Commands

### Basic Operations

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild specific service
docker-compose build backend
docker-compose build frontend
```

### Development

```bash
# Rebuild and restart with latest changes
docker-compose up --build --force-recreate

# View service status
docker-compose ps

# Execute commands in running containers
docker-compose exec backend python -c "print('Hello from backend')"
docker-compose exec frontend npm run lint
```

## Troubleshooting

### Common Issues

1. **Google API Key Error**

   - Ensure your `.env` file contains a valid `GOOGLE_API_KEY`
   - Verify the API key has access to Gemini AI

2. **Port Conflicts**

   - Check if ports 3000 or 8000 are already in use
   - Modify ports in docker-compose.yml if needed

3. **Docker Build Issues**

   - Ensure Docker and Docker Compose are properly installed
   - Clear Docker cache: `docker system prune -a`

4. **Frontend Not Loading**

   - Verify backend API is running and accessible
   - Check browser console for CORS errors

5. **PDF Processing Errors**

   - Ensure PDF files are not corrupted or password-protected
   - Check file size limits

6. **Import Errors**
   - Reinstall dependencies: `pip install -r requirements.txt`
   - Clear Python cache: `find . -name "*.pyc" -delete`

### Performance Optimization

- **Large Documents**: Consider splitting very large PDFs before upload
- **Memory Usage**: Monitor container resource usage with `docker stats`
- **Response Time**: Adjust chunk size and overlap for better performance

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and questions:

- Check the troubleshooting section above
- Review the API documentation at `/docs`
- Open an issue on GitHub
