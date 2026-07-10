# 📄 Conversational RAG PDF Chatbot

A **Conversational Retrieval-Augmented Generation (RAG)** application that allows users to upload multiple PDF documents, ask natural language questions, and receive context-aware answers powered by Large Language Models (LLMs).

The application uses **LangChain** for orchestration, **ChromaDB** as the vector database, **Hugging Face Embeddings** for semantic search, **Groq LLM** for fast inference, and **Streamlit** for an interactive user interface.

---

## 🚀 Features

- 📂 Upload multiple PDF documents
- 💬 Conversational question answering
- 🧠 History-aware retrieval (Conversation Memory)
- 📑 Search within a specific PDF or across all PDFs
- 🗑️ Delete PDFs from the knowledge base
- 📚 Source citations with page numbers
- ⚡ Fast inference using Groq LLM
- 🔍 Semantic search using Hugging Face Embeddings
- 🎨 Interactive Streamlit interface

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### LLM
- Groq
- Llama 3.1

### Framework
- LangChain

### Vector Database
- ChromaDB

### Embedding Model
- sentence-transformers/all-MiniLM-L6-v2

### Document Loader
- PyPDFLoader

### Language
- Python

---

## 📂 Project Structure

```text
Conversational-RAG-PDF-Chatbot/
│
├── app.py
├── chain.py
├── config.py
├── database.py
├── ingest.py
├── llm.py
├── prompts.py
├── retriever.py
├── requirements.txt
├── README.md
│
├── data/
├── chroma_db/
└── screenshots/
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sushma915/conversational-rag-pdf-chatbot.git
```

### 2️⃣ Navigate to the project

```bash
cd conversational-rag-pdf-chatbot
```

### 3️⃣ Create a virtual environment

```bash
python -m venv renv
```

### 4️⃣ Activate the virtual environment

**Windows**

```bash
renv\Scripts\activate
```

**Linux / macOS**

```bash
source renv/bin/activate
```

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.1-8b-instant
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload one or more PDF documents.
2. PDFs are split into smaller chunks.
3. Text chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. The user asks a question.
6. The history-aware retriever rewrites follow-up questions using conversation history.
7. Relevant document chunks are retrieved.
8. The LLM generates an answer using only the retrieved context.
9. Source document names and page numbers are displayed.

---

## 🔮 Future Improvements

- ✅ Excel (.xlsx) support
- ✅ CSV support
- ✅ Word (.docx) support
- ✅ Streaming responses
- ✅ User authentication
- ✅ Cloud vector databases (Pinecone, Milvus, Qdrant)
- ✅ Docker deployment
- ✅ LangGraph integration
- ✅ Multi-user support

---

## 📚 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Conversational AI
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Groq API Integration
- Semantic Search
- Prompt Engineering
- Streamlit
- Python

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👩‍💻 Author

**Thota Sushma**

- 🎓 B.Tech CSE (Artificial Intelligence)
- 💼 Aspiring Machine Learning & Generative AI Engineer
- 🔗 GitHub: https://github.com/sushma915
- 🔗 LinkedIn: https://www.linkedin.com/in/thota-sushma
