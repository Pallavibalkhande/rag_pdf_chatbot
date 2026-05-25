from langchain_text_splitters import RecursiveCharacterTextSplitter


# ✅ Step 1: Better text cleaning
def clean_text(text):
    text = text.replace("\r", "")  # remove carriage return ONLY
    text = text.strip()  # remove extra spaces at start/end
    return text


# ✅ Step 2: Chunking function
def split_documents(documents):

    # ✅ Clean text BEFORE splitting
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=60,
        separators=["\n\n", "\n", ".", " ", ""],  # ✅ VERY IMPORTANT
    )

    docs = splitter.split_documents(documents)

    return docs
