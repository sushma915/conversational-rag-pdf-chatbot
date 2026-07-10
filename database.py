from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

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


def delete_pdf(pdf_name):

    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model
    )

    existing = vector_db.get()

    ids_to_delete = []

    for i, meta in enumerate(existing["metadatas"]):

        if meta["source"] == pdf_name:
            ids_to_delete.append(
                existing["ids"][i]
            )

    if ids_to_delete:
        vector_db.delete(ids=ids_to_delete)
        return True

    return False