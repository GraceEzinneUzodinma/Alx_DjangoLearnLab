from .views import RegisterView, LoginView, TokenView, FollowUserView, UnfollowUserView
from django.urls import path


urlpatterns=[
    path('register/', RegisterView.as_view(), name = 'accounts-register' ),
    path('login/',LoginView.as_view(), name= 'accounts-login'),
    path('Token/', TokenView.as_view(), name= 'accounts-token'),
    path('/follow/<int:user_id>/', FollowUserView.as_view(), name= 'follow'),
    path('/unfollow/<int:user_id>/', UnfollowUserView.as_view, name= 'unfollow')
]