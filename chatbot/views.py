from django.shortcuts import render
from .services.rag_service import ask
import markdown


def home(request):

    question = None
    answer = None

    if request.method == "POST":

        question = request.POST.get("question")

        answer = ask(question)

        answer = markdown.markdown(answer)
    context = {
        "question": question,
        "answer": answer
    }

    return render(
        request,
        "chatbot/home.html",
        context
    )