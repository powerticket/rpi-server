from django import forms
from .models import Question, Answer, Comment, ReComment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['question', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }
