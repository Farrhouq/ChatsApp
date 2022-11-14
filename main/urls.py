from django.urls import path
from .views import *



app_name = 'main'

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('chat/<int:pk>/', chat, name='chat')
]
