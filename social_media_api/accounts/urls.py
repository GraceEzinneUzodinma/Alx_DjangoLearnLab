from .views import RegisterView, LoginView, TokenView
from django.urls import path


urlpatterns=[
    path('Register/', RegisterView.as_view(), name = 'accounts-register' ),
    path('Login/',LoginView.as_view(), name= 'accounts-login'),
    path('Token/', TokenView.as_view(), name= 'accounts-token')
]