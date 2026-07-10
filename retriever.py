from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings #for generating embeddings for user question

from config import EMBEDDING_MODEL, CHROMA_DB_PATH

def get_available_pdfs():

    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model
    )

    existing = vector_db.get()

    pdf_names = {
        meta["source"]
        for meta in existing["metadatas"]
        if "source" in meta
    }

    return ["All Documents"] + sorted(pdf_names)
    
def create_retriever(selected_pdf=None):
    # Load embedding model (saving model)
    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # Load existing ChromaDB
    vector_db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model
    )

    if selected_pdf == "All Documents" or selected_pdf is None:
        # Create Retriever for all documents
        retriever = vector_db.as_retriever(
            search_type = 'mmr',
            search_kwargs={"k": 3, "fetch_k": 10}
        )
    else:
        # Filter by selected document
        retriever = vector_db.as_retriever(
            search_type = 'mmr',
            search_kwargs={"k": 3, "fetch_k": 10, "filter" : {"source":selected_pdf}}
    
        )
    return retriever