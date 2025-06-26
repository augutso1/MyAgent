from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

BACKEND_ROOT = Path(__file__).resolve().parent.parent.parent

CHROMA_PATH = Path("/app/chroma_db") 
CHROMA_PATH.mkdir(exist_ok=True, parents=True)

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

print("Carregando modelo de embedding...")
embedding_function = SentenceTransformer(EMBEDDING_MODEL)
print("Modelo de embedding carregado.")

def get_vector_store():
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    
    collection = client.get_or_create_collection(
        name="documentos_inteligentes",
        embedding_function=None
    )
    
    return collection, embedding_function

def reset_vector_store():
    """
    Apaga a coleção existente para garantir um início limpo.
    """
    print("Resetando o banco de dados vetorial...")
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    
    try:
        client.delete_collection(name="documentos_inteligentes")
        print("Coleção anterior apagada com sucesso.")
    except ValueError:
        print("Nenhuma coleção anterior para apagar.")