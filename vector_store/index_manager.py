from embedding.embedding_model import get_embeddings
from vector_store.faiss_store import create_vector_store
from langchain_community.vectorstores import FAISS
 
 
def build_index(texts):
 
    embeddings = get_embeddings()
 
    vector_store = create_vector_store(texts, embeddings)
 
    vector_store.save_local("vector_db/faiss_index")
 
    return vector_store
 
 
def load_index(path="vector_db/faiss_index"):
 
    embeddings = get_embeddings()
 
    try:
        db = FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )
        return db
    except Exception as e:
        print("Error loading index:", str(e))
        return None