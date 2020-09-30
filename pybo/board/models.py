from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relationship
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # relationship
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relationship
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='comments')
    question = models.ForeignKey(Question, models.CASCADE, blank=True, null=True, related_name='comments')
    answer = models.ForeignKey(Answer, models.CASCADE, blank=True, null=True, related_name='comments')

    def __str__(self):
        return self.content


class ReComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relationship
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='recomments')
    comment = models.ForeignKey(Comment, models.CASCADE, related_name='recomments')

    def __str__(self):
        return self.content
