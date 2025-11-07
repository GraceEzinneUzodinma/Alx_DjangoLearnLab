from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('books/', views.list_books.as_view(), name='book-list-fbv'),
    path('books/', views.LibraryDetailView.as_view(), name='book-list-cbv'),
    path('register/', views.register(template_name='register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]