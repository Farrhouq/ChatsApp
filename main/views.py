from django.shortcuts import render, redirect
from django.conf import settings
from .models import *


# Create your views here.
def chat_list(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    all_chats = Chat.objects.all()
    chats = [chat for chat in all_chats if request.user.email in [chat.user, chat.user1]]

    try:
        pic = request.user.profile_picture.url
    except:
        pic = '../static/images/avatar.svg'

    for chat in chats:
        chat.other = chat.get_other(request)
    context = {'chats': chats, 'pic':pic}
    return render(request, 'chat_list.html', context)
    


def chat(request, pk):
    user = request.user
    chat = Chat.objects.get(id=pk)
    
    if chat is not None:
        friend = chat.user1
        if request.user.email == chat.user1:
            friend = chat.user
        
        if request.method == 'POST':
            message = request.POST.get('message')
            if message:
                Message.objects.create(body=message, chat=chat, user=user)

        friend = User.objects.get(email=friend)
    messages = chat.messages.all()
    context = {'friend':friend, 'messages': messages}
    return render(request, 'chat.html', context)
    
    


