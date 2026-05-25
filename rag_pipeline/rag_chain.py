from rag_pipeline.retrieval import retrieve_docs
from rag_pipeline.context_handler import build_context
from rag_pipeline.prompt_builder import build_prompt
from llm.llm_client import get_llm


def run_rag_pipeline(query):

    docs = retrieve_docs(query)

    context = build_context(docs)

    prompt = build_prompt(query, context)

    # ✅ Get LLM
    llm = get_llm()

    # ✅ Call LLM properly
    response = llm.invoke(prompt)

    return response.content
