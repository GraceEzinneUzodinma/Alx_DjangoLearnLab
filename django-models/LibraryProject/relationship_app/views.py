from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
def list_books(request):
      books = Book.objects.all()  
      context = {'book_list': books}  
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
  model = Book
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'books'
class SignUpView(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'

def Admin(user):
    return user.userprofile.role == 'Admin'
@user_passes_test(Admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

def Librarian(user):
    return user.userprofile.role == 'Librarian'
@user_passes_test(Librarian)
def Librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

def Member(user):
    return user.userprofile.role == 'Member'
@user_passes_test(Member)
def Member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required("relationship_app.can_add_book")
def add_book(request):
    return HttpResponse("you have permission to add a book")
@permission_required("relationship_app.can_change_book")
def change_book(request):
    return HttpResponse("you have permission to change the book")
@permission_required("relationship_app.can_delete_book")
def delete_book(request):
    return HttpResponse("you have permission to delete a book")
