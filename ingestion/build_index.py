from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    "django_docs/docs/ref",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={
        "encoding": "utf-8"
    },
)

documents = loader.load()




from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200,

)

chunks = splitter.split_documents(documents)




from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector = embeddings.embed_query("What is Django?")




from langchain_chroma import Chroma

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vector_store",
)

retriever = vector_store.as_retriever()

results = retriever.invoke(
    "What is select_related()?"
)

print(len(results))

print(results[0].metadata)

print(results[0].page_content)