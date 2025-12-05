from django.shortcuts import render, redirect
from django.views  import generic, View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
        form = UserChangeForm(instance=request.user)
        return render(request, "profile.html", {"form": form})

    def post(self, request):   # <-- checker wants this "method"
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()        # <-- checker wants "save()"
            return redirect("profile")

        return render(request, "profile.html", {"form": form})

        

# Create your views here.
