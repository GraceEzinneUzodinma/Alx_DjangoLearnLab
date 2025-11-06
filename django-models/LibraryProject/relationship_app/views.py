from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from .models import Library
def book_list(request):
      books = Book.objects.all()  
      context = {'book_list': books}  
      return render(request, 'relationship_app/list_books.html', context)

class BookListView(ListView):
  model = Book
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'books'