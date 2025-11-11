from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def Librarian(user):
    return user.userprofile.role == 'Librarian'
@user_passes_test(Librarian)
def Librarian_view(request):
    return render(request, "librarian_view.html")
