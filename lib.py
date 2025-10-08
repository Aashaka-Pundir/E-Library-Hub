from django import forms
from .models import Story
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', 'category', 'published']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
