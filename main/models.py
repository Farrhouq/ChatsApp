from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=200, null=True, verbose_name='username')
    username = models.EmailField(unique=True, max_length=200, verbose_name='email address')
    profile_picture = models.ImageField(default='avatar.svg', null=True, blank=True)

    def read_message(self, message) -> None:
        if self.email == message.chat.user:
            message.read = True
        else:
            message.read1 = True
        message.save()

    def __str__(self) -> str:
        return self.email
    
    
class Chat(models.Model):
    user = models.CharField(max_length=200)
    user1 = models.CharField(max_length=200)

    def get_other(self, request):
        user_list = [self.user, self.user1]
        return user_list[user_list.index(request.user.email)-1]

    def user_unread(self):
        user = User.objects.get(email=self.user1)
        return self.messages.filter(read=False, user=user).count()

    def user1_unread(self):
        user = User.objects.get(email=self.user)
        return self.messages.filter(read1=False, user=user).count()

    def get_last_message(self):
        return self.messages.all().last()

    other = None
    user_unread_ = None
    last_message = None
    
    def __str__(self) -> str:
        return f"{self.user} | {self.user1}"


class Message(models.Model):
    body = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    read = models.BooleanField(null=True, default=False)
    read1 = models.BooleanField(null=True, default=False)

    def get_user(self):
        return self.chat.user

    def get_user1(self):
        return self.chat.user1

    def __str__(self) -> str:
        return self.body[0:20]