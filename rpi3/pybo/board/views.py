from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm, CommentForm, ReCommentForm
from .models import Question, Answer, Comment, ReComment
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
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('board:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'board/form.html', context)


@require_safe
def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    comment_form = CommentForm()
    context = {
        'question': question,
        'answers': answers,
        'comment_form': comment_form,
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
    return render(request, 'board/form.html', context)


@require_POST
def delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('board:index')


# # # # # # # # # # Question CRUD end # # # # # # # # # #



# # # # # # # # # # Answer CRUD start # # # # # # # # # #


def create_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('board:detail', pk)
    else:
        answer_form = AnswerForm()
    context = {
        'question': question,
        'form': answer_form,
    }
    return render(request, 'board/form.html', context)


@require_POST
def delete_answer(request, question_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    answer.delete()
    return redirect('board:detail', question_pk)


# # # # # # # # # # Answer CRUD end # # # # # # # # # #



# # # # # # # # # # Comment CRUD start # # # # # # # # # #


def create_question_comment(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            return redirect('board:detail', pk)
    else:
        comment_form = CommentForm()
    context = {
        'question': question,
        'answers': answers,
        'comment_form': comment_form,
    }
    return render(request, 'board/detail.html', context)


def create_answer_comment(request, pk, answer_pk):
    question = get_object_or_404(Question, pk=pk)
    answer = get_object_or_404(Answer, pk=pk)
    answers = question.answer_set.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            return redirect('board:detail', pk)
    else:
        comment_form = CommentForm()
    context = {
        'question': question,
        'answers': answers,
        'comment_form': comment_form,
    }
    return render(request, 'board/detail.html', context)


def delete_question_comment(request, pk, comment_pk):
    pass


def delete_answer_comment(request, pk, answer_pk, comment_pk):
    pass


# # # # # # # # # # Comment CRUD end # # # # # # # # # #
