from relationship_app.models import Author, Book, Library, Librarian
Book.objects.filter(author__name ='')
Book.library.all()
Library.objects.get(name=library_name)
books.all()