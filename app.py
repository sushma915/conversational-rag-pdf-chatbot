import os
import streamlit as st
from config import DATA_PATH
from ingest import ingest_pdf
from chain import create_chain
from database import get_available_pdfs, delete_pdf
from langchain_core.messages import (
    HumanMessage, 
    AIMessage
)

st.title("📄 RAG PDF Question Answering")

if "messages" not in st.session_state:# it is a temporary memory for streamlit 
    st.session_state.messages = []

def get_chat_history():

    chat_history = []

    for message in st.session_state.messages:

        if message["role"] == "user":
            chat_history.append(
                HumanMessage(content=message["content"])
            )

        else:
            chat_history.append(
                AIMessage(content=message["content"])
            )
    return chat_history 

uploaded_files = st.file_uploader(
    "Upload a PDF Files",
    type="pdf",
    accept_multiple_files = True
)


if uploaded_files:
    for uploaded_file in uploaded_files:

        pdf_path = os.path.join(
            DATA_PATH,
            uploaded_file.name
        )

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        added = ingest_pdf(pdf_path)
        if added:
            st.success(f"Added {uploaded_file.name}!")
        else:
            st.info(f"{uploaded_file.name} already exists.")

    st.success("Knowledge Base updated!")
    st.rerun()

pdf_names = get_available_pdfs()

st.caption(f"📚 {len(pdf_names) - 1} PDF(s) in Knowledge Base")

if len(pdf_names) > 1:

    selected_pdf = st.selectbox(
        "📄 Search In",
        pdf_names
    )
    st.divider()

    delete_pdf_name = st.selectbox(
        "🗑 Delete PDF",
        pdf_names[1:]      # Skip "All Documents"
    )

    if st.button("🗑 Delete Selected PDF"):

        if delete_pdf(delete_pdf_name):

            st.session_state.messages = []

            st.success(f"{delete_pdf_name} deleted successfully.")

            st.rerun()

        else:
            st.error("Unable to delete PDF.")

    st.divider()

    rag_chain = create_chain(selected_pdf)

else:
    st.info("📄 Upload a PDF to start asking questions.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask your question...")

if question:

    if len(pdf_names) <= 1:
        st.warning("Please upload at least one PDF.")

    else:

        with st.chat_message("user"):
            st.write(question)

        chat_history = get_chat_history()

        try:
            with st.spinner("Thinking..."):
                response = rag_chain.invoke(
                    {
                        "input": question,
                        "chat_history": chat_history
                    }
                )
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        answer = response["answer"]
        docs = response["context"]
        
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.write(answer)

        # Sources
        with st.expander("📄 Sources"):

            shown_sources = set()

            for doc in docs:

                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", "N/A")

                source_info = f"{source} (Page {page + 1})"

                if source_info not in shown_sources:
                    st.write(f"• {source_info}")
                    shown_sources.add(source_info)