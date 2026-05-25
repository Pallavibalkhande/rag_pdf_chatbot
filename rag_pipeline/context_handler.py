def build_context(docs):
    return "\n".join([doc.page_content for doc in docs])