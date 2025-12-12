from django.shortcuts import render
# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
)

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({
                "message": "Registration successful",
                "username": user.username,
                "email": user.email,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": "Login successful",
                "username": serializer.validated_data["username"],
                "token": serializer.validated_data["token"]
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({"token": token.key})

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = self.get_object()
        request.user.following.add(user)
        return Response({"detail": "Followed"})

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = self.get_object()
        request.user.following.remove(user)
        return Response({"detail": "Unfollowed"})
# Create your views here.
