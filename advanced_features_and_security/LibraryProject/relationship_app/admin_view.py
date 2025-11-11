from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def Admin(user):
    return user.userprofile.role == 'Admin'
@user_passes_test(Admin)
def admin_view(request):
    return render(request, "admin_view.html")

