from django.urls import path, include
from .views import UserRegisterView, ProfileUpdateView, BlogCreateView,BlogDeleteView, BlogDetailView, BlogUpdateView, BlogListView
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('post/<int:pk>/detail/', BlogDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='post-update'),
    path('post/list/', BlogListView.as_view(), name= 'post-list'),
]