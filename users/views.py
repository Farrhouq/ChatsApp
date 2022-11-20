from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout, authenticate, views as auth_views
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import *
from .models import *
from main.models import Chat, User

# User = settings.AUTH_USER_MODEL


# Create your views here.
def loginUser(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("main:chat_list")
    form = UserForm()
    if request.method == "POST":
        email = str(request.POST.get("email")).lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=email)
        except:
            user = None

        in_user = authenticate(username=email, password=password)

        if in_user is not None:
            login(request, user)
            return redirect('main:chat_list')
        else:
            if user is None:
                messages.error(request, 'The user does not exist')
            else:
                messages.error(request, 'Your password is incorrect')
    context = {"form": form, "page": page}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('users:login')


def register(request):
    page = "register"
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("main:chat_list")

    context = {
        "form": form,
        "page": page,
    }
    return render(request, "register.html", context)


def user_profile(request):
    user = request.user
    chats = [
        chat for chat in Chat.objects.all()
        if request.user.email in [chat.user, chat.user1]
    ]

    try:
        pic = request.user.profile_picture.url
    except:
        pic = '../static/images/avatar.svg'

    for chat in chats:
        chat.other = chat.get_other(request)

    context = {'chat_number': len(chats), 'pic': pic}
    return render(request, 'user_profile.html', context)


def edit_profile(request):
    user = request.user
    profile_picture = None

    all_chats = Chat.objects.all()
    chats_one = [chat for chat in all_chats if request.user.email == chat.user]
    chats_two = [
        chat for chat in all_chats if request.user.email == chat.user1
    ]

    form = UserEditForm(instance=user)
    context = {'form': form}
    if request.method == 'POST':
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile_picture')
        try:
            user.email = email
            user.profile_picture = profile_picture
            user.username = request.POST.get('username')
            user.save()

            for chat in chats_one:
                chat.user = email
                chat.save()

            for chat in chats_two:
                chat.user1 = email
                chat.save()

            messages.success(request, 'Profile updated successfully!')
            return redirect('main:chat_list')
        except:
            messages.error(request, 'An error occured!')

    return render(request, 'edit_profile.html', context)


class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request,
                         'Your password has been changed successfully!')
        return super().form_valid(form)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/reset/password_reset_subject.txt"
                    c = {
                        "email": user.username,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject,
                                  email,
                                  'admin@example.com', [user.username],
                                  fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_done")
                    # return redirect ("users:user_profile")
    password_reset_form = PasswordResetForm()
    return render(request=request,
                  template_name="registration/reset/password_reset_form.html",
                  context={"form": password_reset_form})
