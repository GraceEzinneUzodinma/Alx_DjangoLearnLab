from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser, Book
from django.contrib.auth.decorators import permission_required


def create_groups():
    # Get the content type for your custom user model
    content_type = ContentType.objects.get_for_model(CustomUser)

    # Fetch the permissions (these must already exist in your model's Meta)
    can_view = Permission.objects.get(codename='can_view', content_type=content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=content_type)

    # Create groups (if they don’t exist)
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    editors_group, _ = Group.objects.get_or_create(name='Editors')
    admins_group, _ = Group.objects.get_or_create(name='Admins')

    # Assign permissions to groups
    viewers_group.permissions.set([can_view])
    editors_group.permissions.set([can_view, can_edit, can_create])
    admins_group.permissions.set([can_view, can_edit, can_create])  # add more if needed

    print("Groups and permissions successfully created!")

@permission_required('your_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')

    return render(request, 'books/create_book.html')

@permission_required('your_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

@permission_required('your_app.can_view', raise_exception=True)
def list_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
# Create your views here.
