from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder #for making the prompt dynamic we use this

CONTEXTUALIZE_Q_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Given a chat history and the latest user question, "
            "rewrite the question so it can be understood without the chat history. "
            "Do NOT answer the question. Only rewrite it if needed."
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the context below to answer the user's question.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Context:
{context}
"""
        ),

        MessagesPlaceholder("chat_history"),

        ("human", "{input}")
    ]
)