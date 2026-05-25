def build_prompt(query, context):
    return f"""
    You are an assistant. Answer ONLY using the context below.

    Context:
    {context}

    Question:
    {query}
    """