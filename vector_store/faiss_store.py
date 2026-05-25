from langchain_community.vectorstores import FAISS
from embedding.embedding_utils import embed_texts

def create_vector_store(texts, embeddings):

    vectors = embed_texts(embeddings, texts)

    db = FAISS.from_embeddings(
        list(zip(texts, vectors)),
        embeddings
    )

    return db
