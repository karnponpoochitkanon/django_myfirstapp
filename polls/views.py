from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": q})

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": q})

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        choice = q.choice_set.get(pk=request.POST["choice"])
    except Exception:
        return render(request, "polls/detail.html", {
            "question": q,
            "error_message": "You didn't select a choice."
        })
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse("results", args=(q.id,)))