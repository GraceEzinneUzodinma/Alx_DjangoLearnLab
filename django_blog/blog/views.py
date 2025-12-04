from django.shortcuts import render
from django.views  import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template = 'blog/register.html'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'profile_picture']

class EmailUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        profile_form = ProfileForm(instance=request.user.profile)
        email_form = EmailUpdateForm(instance=request.user)

        return render(request, 'profile.html', {
            'profile_form': profile_form,
            'email_form': email_form,
        })

    def post(self, request):
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        email_form = EmailUpdateForm(
            request.POST,
            instance=request.user
        )

        

# Create your views here.
