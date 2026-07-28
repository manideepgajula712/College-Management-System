from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer
)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer