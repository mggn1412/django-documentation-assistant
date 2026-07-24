# Django Documentation Assistant

A Retrieval-Augmented Generation (RAG) chatbot built with Django, LangChain, ChromaDB and Google Gemini that answers questions using the official Django documentation.

---

## Features

- Retrieval-Augmented Generation (RAG)
- LangChain LCEL pipelines
- Chroma vector database
- HuggingFace embeddings
- Google Gemini integration
- Django web interface
- Answers only using the official Django documentation
- Returns "I don't know" when the answer is not found in the knowledge base

---

## Tech Stack

- Python
- Django
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Google Gemini
- Git

---

## How it works

1. The official Django documentation is cloned locally.
2. The documentation is split into chunks.
3. Embeddings are generated for every chunk.
4. ChromaDB stores the embeddings.
5. When the user asks a question, the retriever finds the most relevant chunks.
6. Those chunks are sent to Google Gemini.
7. Gemini generates the final answer using only the retrieved context.

## Project Structure

```
django-documentation-assistant/

├── chatbot/
│   ├── services/
│   ├── templates/
│   └── views.py
│
├── config/
│
├── ingestion/
│   └── build_index.py
│
├── vector_store/      (generated)
├── django_docs/       (generated)
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mggn1412/django-documentation-assistant.git
cd django-documentation-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## Download the Django Documentation

Clone the official Django repository:

```bash
git clone --depth 1 https://github.com/django/django.git django_docs
```

The documentation used by the chatbot is located in:

```
django_docs/docs/
```

---

## Build the Vector Database

Generate the embeddings and Chroma vector store:

```bash
python ingestion/build_index.py
```

This creates the `vector_store/` directory.

> **Note:** `vector_store/` is intentionally ignored by Git because it can always be regenerated from the official documentation.

---

## Run the Project

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

## Example Questions

- What is select_related?
- How do Django migrations work?
- What is ModelForm?
- What is the difference between prefetch_related and select_related?
- How do middleware work?

Questions unrelated to Django should return:

```
I don't know.
```

---



## Architecture

```
User

↓

Django View

↓

Retriever

↓

ChromaDB

↓

Relevant Documentation Chunks

↓

Prompt

↓

Google Gemini

↓

Answer
```

---

## Future Improvements

- Conversation memory
- Source citations
- Streaming responses
- Better UI
- Docker support
- Deployment
- Unit tests

---

## License

MIT