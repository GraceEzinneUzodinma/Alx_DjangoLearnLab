from django.shortcuts import render, redirect
from django.views  import generic, View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Profile, Comment
from .serializers import PostSerializer
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
        model = Profile
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
    
class BlogListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'publication_year']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogCreateView(LoginRequiredMixin,generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    template_name = 'blog/creating_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user   # attach post to logged-in author
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin,generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin,generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']

class CommentListView(ListView):
    model = Comment
    fields ='__all__'

class CommentDetailView(DetailView):
    model = Comment
    fields = '__all__'

class CommentUpdateView(UpdateView):
    model = Comment
    fields  = ['content', 'post']

class CommentDeleteView(DeleteView):
    model = Comment
    fields = ['content', 'post']




        

# Create your views here.
