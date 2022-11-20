from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
    path('register', register, name='register'),
    path('user_profile', user_profile, name='user_profile'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path("password-reset/", password_reset_request, name="password-reset"),
    path('change-password/',
         CustomPasswordChangeView.as_view(),
         name='change_password'),
]