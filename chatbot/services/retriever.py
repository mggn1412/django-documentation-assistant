from langchain_chroma import Chroma

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    persist_directory="vector_store",
    embedding_function=embeddings,
)

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 4
    }
)