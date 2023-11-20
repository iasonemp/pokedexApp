from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Comment

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']