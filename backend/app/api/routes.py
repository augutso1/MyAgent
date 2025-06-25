from fastapi import APIRouter, UploadFile, File
from app.schemas.chat import ChatRequest, ChatResponse, UploadResponse

router = APIRouter(prefix="/api/v1")

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/chat", response_model=ChatResponse)
def chat_query(request: ChatRequest):
    print(request.question)
    return ChatResponse(
        #TODO Enviar pergunta para o modelo
        #TODO Identificar fonte dentro dos documentos upados
    )

@router.post("/upload", response_model=UploadResponse)
def upload_query(file: UploadFile = File(...)):
    return UploadResponse(
        filename=file.name,
        message="Arquivo recebido"
    )