import os
from config import DATA_PATH
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma #store generated embedding in chromadb
from config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBEDDING_MODEL,
    CHROMA_DB_PATH
)
def ingest_pdf(pdf_path):
    # Step 1: Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Step 2: Chunking
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents(documents)
    #adding meta data
    for chunk in chunks:
        chunk.metadata['source']=os.path.basename(pdf_path) #basename returns only file name
    # Step 3: Embedding Model
    embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
    )
     # Step 4: if chromdb present add to that otherwise create new
    if os.path.exists(CHROMA_DB_PATH):
        vector_db = Chroma( #open existing database
            persist_directory=CHROMA_DB_PATH,
            embedding_function=embedding_model,
            )

        existing = vector_db.get() # read existing metadata

        existing_sources = {
            meta["source"]
            for meta in existing["metadatas"]
            if "source" in meta
        }

        current_pdf = os.path.basename(pdf_path)

        if current_pdf in existing_sources:
            print(f"{current_pdf} already exists. Skipping...")
            return False    

        vector_db.add_documents(chunks)

        print("Chunks Added to Existing Database")
        return True
    else:
    # Step 4: store in ChromaDB
        Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory= CHROMA_DB_PATH #store embedding in this folder
        )

        print("Vector Database Created Successfully!")