from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def Member(user):
    return user.userprofile.role == 'Member'
@user_passes_test(Member)
def Member_view(request):
    return render(request, "member_view.html")
