from .views import RegisterView, LoginView, TokenView
from django.urls import path


urlpatterns=[
    path('register/', RegisterView.as_view(), name = 'accounts-register' ),
    path('login/',LoginView.as_view(), name= 'accounts-login'),
    path('Token/', TokenView.as_view(), name= 'accounts-token')
]