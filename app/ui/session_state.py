import streamlit as st

def init_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_message(role, message):
    st.session_state.chat_history.append((role, message))