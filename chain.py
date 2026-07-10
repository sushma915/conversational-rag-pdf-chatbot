from langchain_core.output_parsers import StrOutputParser # for giving the output it converts in the form of clean string
from langchain_core.runnables import RunnablePassthrough #it sends the input with changing

from config import *
from llm import get_llm
from retriever import create_retriever
from prompts import RAG_PROMPT, CONTEXTUALIZE_Q_PROMPT
from ingest import ingest_pdf 

from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain
)

from langchain.chains.combine_documents import (
    create_stuff_documents_chain
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_chain(selected_pdf=None):

    retriever = create_retriever(selected_pdf)
    llm = get_llm()

    # Step 1: Create History Aware Retriever
    history_aware_retriever = create_history_aware_retriever(
        llm,
        retriever,
        CONTEXTUALIZE_Q_PROMPT
    )

    # Step 2: Create Document Chain
    document_chain = create_stuff_documents_chain(
        llm,
        RAG_PROMPT
    )

    # Step 3: Create Retrieval Chain
    rag_chain = create_retrieval_chain(
        history_aware_retriever,
        document_chain
    )

    return rag_chain