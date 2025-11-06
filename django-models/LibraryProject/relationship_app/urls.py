from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', views.list_books.as_view(), name='book-list-fbv'),
    path('books/', views.LibraryDetailView.as_view(), name='book-list-cbv'),
]