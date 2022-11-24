from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from django.contrib import messages


# Create your views here.
def chat_list(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            if username == request.user.email:
                messages.error(request,
                               "Can't create a chat with your username")
            elif not User.objects.filter(email=request.user.email).exists(
            ) or not User.objects.filter(email=username).exists():
                messages.error(request,
                               'This user is not registered on ChatsApp')
            else:
                try:
                    Chat.objects.create(user=request.user.email,
                                        user1=username)
                    messages.success(
                        request,
                        f'The chat "{username}" was added successfully!')
                except ValidationError:
                    messages.error(request, 'This chat already exists')

    all_chats = Chat.objects.all()
    chats = [
        chat for chat in all_chats
        if request.user.email in [chat.user, chat.user1]
    ]

    try:
        pic = request.user.profile_picture.url
    except:
        pic = '../static/images/avatar.svg'

    unread_chats_count = 0
    for chat in chats:
        chat.other = chat.get_other(request)
        if chat.user1 == request.user.email:
            chat.user_unread_ = chat.user1_unread()
        else:
            chat.user_unread_ = chat.user_unread()
        chat.save()

        if chat.user_unread_:
            unread_chats_count += 1
        try:
            chat.other_pic = User.objects.get(
                email=chat.other).profile_picture.url
        except:
            chat.other_pic = 'media/images/avatar.svg'

    if unread_chats_count:
        label = f'Chats ({unread_chats_count})'
    else:
        label = 'Chats'

    context = {'chats': chats, 'pic': pic, 'label': label}
    return render(request, 'chat_list.html', context)


def chat(request, pk):
    user = request.user
    chat = Chat.objects.get(id=pk)

    friend = chat.user1
    if request.user.email == chat.user1:
        friend = chat.user

    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Message.objects.create(body=message, chat=chat, user=user)

    messages = chat.messages.all()
    message_list = []
    for message in messages:
        user.read_message(message)
        message_list.append(message)

    for message in message_list:
        if message_list.index(message) + 1 != len(
                message_list) and message_list[message_list.index(message) +
                                               1].user == message.user:
            message.message_margin = '0px'
        pass

    friend = User.objects.get(email=friend)

    context = {
        'friend': friend,
        'messages': messages,
    }
    return render(request, 'chat.html', context)


def delete_chat(request, pk):
    chat = Chat.objects.get(id=pk)
    message_count = chat.messages.count()
    message = ' and one message'
    chat_name = chat.get_other(request)

    if message_count > 1:
        message = f' and all its {message_count} messages'
    elif not message_count:
        message = ''

    if request.method == 'POST':
        chat.delete()
        messages.success(request,
                         f'The chat "{chat_name}" was deleted successfully!')
        return redirect('main:chat_list')
    return render(request, 'delete.html', {'message': message})
