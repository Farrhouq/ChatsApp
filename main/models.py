from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=200, null=True, verbose_name='username')
    username = models.EmailField(unique=True, max_length=200, verbose_name='email address')
    profile_picture = models.ImageField(default='avatar.svg', null=True, blank=True)
    # first_name = models.CharField(null=True, max_length=50, verbose_name='name')

    def __str__(self) -> str:
        return self.email
    
    
class Chat(models.Model):
    user = models.CharField(max_length=200)
    user1 = models.CharField(max_length=200)

    def get_other(self, request):
        return [self.user, self.user1][[self.user, self.user1].index(request.user.email)-1]
        
    other = None
    
    def __str__(self) -> str:
        return f"{self.user} | {self.user1}"


class Message(models.Model):
    body = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.body[0:20]