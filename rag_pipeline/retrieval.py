
import os
from vector_store.index_manager import load_index
from vector_store.retriever import get_retriever


def retrieve_docs(query):

    if not os.path.exists("vector_db/faiss_index"):
        return []

    store = load_index("vector_db/faiss_index")

    retriever = get_retriever(store)

    return retriever.invoke(query)