from pydantic import BaseModel, Field
#Chat schemas
class ChatRequest(BaseModel):
    question: str = Field(
        min_length=0,
        max_length=200
    )

class ChatResponse(BaseModel):
    answer: str
    source_found: bool

#Upload schema
class UploadResponse(BaseModel):
    filename: str
    message: str