from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *
from django.contrib.auth import login, logout, authenticate
from .models import *


# User = settings.AUTH_USER_MODEL

# Create your views here.
def loginUser(request):
    page = "login"
    # if request.user.is_authenticated:
    #     return redirect("home")

    form = UserForm()
    if request.method == "POST":
        email = str(request.POST.get("email"))
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=email)
        except:
            pass

        in_user = authenticate( username=email, password=password)
        
        if in_user is not None:
            login(request, user)
            return redirect('main:chat_list')
        else:
            pass
            # return redirect("register")
            
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
    
    context = {"form": form, "page": page,}
    return render(request, "register.html", context)