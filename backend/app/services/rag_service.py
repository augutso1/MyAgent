import shutil
from pathlib import Path
from fastapi import UploadFile
import pypdf
from app.storage.vector_store import get_vector_store
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Chave de API do Google não encontrada. Verifique seu arquivo .env")

genai.configure(api_key=GOOGLE_API_KEY)

llm_model = genai.GenerativeModel('gemini-2.0-flash')

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True, parents=True)

#Processamento do arquivo PDF upado
async def process_and_index_document(file: UploadFile):

    file_path = DATA_PATH / file.filename
    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"Arquivo '{file.filename}' salvo em '{file_path}'")
    finally:
        file.file.close()

    try:
        print(f"Extraindo texto do arquivo '{file.filename}'...")
        reader = pypdf.PdfReader(file_path)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()
        
        print("Texto extraído com sucesso!")
        
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        file_path.unlink()
        raise
    print("Dividindo o texto em chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=pdf_text)
    print(f"Texto dividido em {len(chunks)} chunks.")

    print("Obtendo o banco de dados vetorial e indexando os chunks...")
    collection, embedding_function = get_vector_store()

    embeddings = embedding_function.encode(chunks).tolist()
    
    ids = [f"{file.filename}-{i}" for i, _ in enumerate(chunks)]

    collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=ids
    )

    print(f"🎉 Processamento e indexação do arquivo '{file.filename}' concluídos com sucesso!")

#Implementação do RAG com API do Gemini
def query_rag(query_text: str) -> str:
    collection, embedding_function = get_vector_store()

    query_embedding = embedding_function.encode(query_text).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context_chunks = results['documents'][0]
    context = "\n\n---\n\n".join(context_chunks)

    prompt_template = f"""
    Você é um assistente de IA especialista em análise de documentos.
    Sua tarefa é responder à pergunta do usuário estritamente com base no contexto fornecido.
    Se a informação não estiver no contexto, responda: "Com base nos documentos fornecidos, não encontrei informações sobre isso."

    Contexto:
    {context}

    ---

    Pergunta: {query_text}

    Resposta:
    """

    try:
        print("Enviando prompt para o Gemini...")
        response = llm_model.generate_content(prompt_template)
        print("Resposta recebida do Gemini.")
        
        return response.text
        
    except Exception as e:
        print(f"Erro ao gerar resposta com o Gemini: {e}")
        return "Ocorreu um erro ao tentar gerar a resposta. Por favor, tente novamente."
