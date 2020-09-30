from django.shortcuts import render, redirect, get_object_or_404
from ..forms import QuestionForm, AnswerForm, CommentForm, ReCommentForm
from ..models import Question, Answer, Comment, ReComment
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


# # # # # # # # # # Question CRUD start # # # # # # # # # #


@require_safe
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'board/index.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('board:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'board/question.html', context)


@require_safe
def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'board/detail.html', context)


@require_http_methods(['POST', 'GET'])
def update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect('board:detail', question.pk)
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form,
    }
    return render(request, 'board/question.html', context)


@require_POST
def delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('board:index')


# # # # # # # # # # Question CRUD end # # # # # # # # # #