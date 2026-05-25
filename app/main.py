import streamlit as st
import tempfile
import sys
import os

# ✅ Fix project path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

# ✅ Imports
from data_processing.pdf_loader import load_pdf
from data_processing.chunking import split_documents

from vector_store.index_manager import build_index
from rag_pipeline.rag_chain import run_rag_pipeline

# ✅ Title
st.title("📄 RAG PDF Chatbot")

# ✅ Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")


if uploaded_file:

    # ✅ Process only once per file
    if (
        "file_name" not in st.session_state
        or st.session_state.file_name != uploaded_file.name
    ):

        st.session_state.file_name = uploaded_file.name

        # ✅ Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        st.success("✅ PDF Uploaded")

        # ✅ Load + split PDF
        documents = load_pdf(file_path)
        docs = split_documents(documents)

        texts = [doc.page_content for doc in docs]

        # ✅ Build FAISS index
        build_index(texts)

    # ✅ Initialize session state for query
    if "submitted_query" not in st.session_state:
        st.session_state.submitted_query = None

    # ✅ Callback function to handle Enter key press
    def submit_query():
        st.session_state.submitted_query = st.session_state.query_input

    # ✅ Input (Submit on Enter key - no button)
    st.text_input(
        "Ask your question:",
        key="query_input",
        placeholder="Type your question and press Enter...",
        on_change=submit_query,
    )

    # ✅ Process query if submitted
    if st.session_state.submitted_query:
        query = st.session_state.submitted_query

        # ✅ DIRECTLY CALL RAG pipeline
        answer = run_rag_pipeline(query)

        st.write("### ✅ Answer:")
        st.write(answer)

        # ✅ Reset for next query
        st.session_state.submitted_query = None

else:
    st.info("Upload a PDF to start")
