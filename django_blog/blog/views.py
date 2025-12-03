from django.shortcuts import render
from django.views  import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template = 'blog/register.html'



# Create your views here.
