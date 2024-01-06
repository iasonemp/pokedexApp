from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Comment
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
                    'username': forms.TextInput(attrs={'autocomplete': 'off'}),
                    'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
                }
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment',
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write your comment'}),
        }