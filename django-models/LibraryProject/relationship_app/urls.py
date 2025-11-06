from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list.as_view(), name='book-list-fbv'),
    path('books/', views.BookListView.as_view(), name='book-list-cbv'),
]