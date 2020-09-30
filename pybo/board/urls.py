from django.urls import path
from . import views


app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    
    # Question CRUD
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    
    # Answer CRUD
    path('<int:pk>/answer/create/', views.create_answer, name='create_answer'),
    path('<int:question_pk>/answer/<int:answer_pk>/delete/', views.delete_answer, name='delete_answer'),

    # Comment CRUD
    path('<int:pk>/comment/create/', views.create_question_comment, name='create_question_comment'),
    path('<int:pk>/answer/<int:answer_pk>/comment/create/', views.create_answer_comment, name='create_answer_comment'),
    path('<int:pk>/comment/<int:comment_pk>/delete/', views.delete_question_comment, name='delete_question_comment'),
    path('<int:pk>/answer/<int:answer_pk>/comment/<comment_pk>/delete/', views.delete_answer_comment, name='delete_answer_comment'),
    
    # ReComment CRUD
]
