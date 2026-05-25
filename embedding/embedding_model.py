from langchain_openai import OpenAIEmbeddings
from config.config import API_KEY, BASE_URL
 
def get_embeddings():
    return OpenAIEmbeddings(
        model="amazon.titan-embed-text-v1",
        base_url=BASE_URL,
        api_key=API_KEY,
        check_embedding_ctx_length=False
    )