from django.urls import path
from .views import *



app_name = 'main'

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('chat/<int:pk>/', chat, name='chat'), 
    path('delete_chat/<int:pk>/', delete_chat, name='delete_chat'),
    path('delete_message/<int:pk>/', delete_message, name='delete_message'),
]
