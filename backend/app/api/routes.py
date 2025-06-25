from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse, UploadResponse
from app.services import rag_service

router = APIRouter(prefix="/api/v1")

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/chat", response_model=ChatResponse)
def chat_query(request: ChatRequest):
    answer_text = rag_service.query_rag(request.question)
    return ChatResponse(
        answer=answer_text,
        source_found=True
    )

@router.post("/query", response_model=ChatResponse, tags=["RAG"])
def post_query(request: ChatRequest):
    answer_text = rag_service.query_rag(request.question)
    
    return ChatResponse(
        answer=answer_text,
        source_found=True
    )

@router.post("/upload", response_model=UploadResponse)
async def upload_query(file: UploadFile = File(...)):
    try:
        await rag_service.process_and_index_document(file)
        
        return UploadResponse(
            filename=file.filename,
            message="Arquivo recebido e enviado para processamento."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo: {str(e)}")