from langchain_core.output_parsers import StrOutputParser

from .llm_service import llm

from .retriever import retriever

from .prompts import RAG_PROMPT

parser = StrOutputParser()

def ask(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    chain = RAG_PROMPT | llm | parser

    response = chain.invoke({

        "context": context,

        "question": question,

    })

    return response