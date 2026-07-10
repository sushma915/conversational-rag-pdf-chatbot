
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM Model
MODEL_NAME = "llama-3.3-70b-versatile"

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chroma Database Folder
CHROMA_DB_PATH = "chroma_db"

# Data Folder
DATA_PATH = "data"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100