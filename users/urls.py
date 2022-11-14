from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
    path('register', register, name='register')
]