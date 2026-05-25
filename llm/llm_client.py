from langchain_openai import ChatOpenAI
from config.config import API_KEY, BASE_URL

def get_llm():
    return ChatOpenAI(
        openai_api_key=API_KEY,
        base_url=BASE_URL,
        model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    )