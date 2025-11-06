from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
def book_list(request):
      books = Book.objects.all()  
      context = {'book_list': books}  
      return render(request, 'list_books.html', context)

class BookListView(ListView):
  model = Book
  template_name = 'library_detail.html'
  context_object_name = 'books'