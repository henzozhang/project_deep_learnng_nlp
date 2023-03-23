from django.urls import path
from . import views

urlpatterns = [
    path('chatbox/', views.chatbox, name = 'chatbox'),
    path('chatbox2/', views.chatbox2, name = 'chatbox2'),
]