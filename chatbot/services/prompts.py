from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert Django assistant.

Answer ONLY using the context below.

If the answer is not contained in the context, say that you don't know.

Context:

{context}

Question:

{question}
"""
)