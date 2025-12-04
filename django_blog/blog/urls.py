from django.urls import path, include
from .views import UserRegisterView
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]