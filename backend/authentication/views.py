from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdmin, IsFaculty, IsStudent

from .models import User

from .serializers import (
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
    UserManagementSerializer
)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "role": user.role.name if user.role else None,
        })


class StudentDashboardView(APIView):

    permission_classes = [IsStudent]

    def get(self, request):

        return Response({
            "message": "Welcome Student",
            "user": request.user.username
        })


class FacultyDashboardView(APIView):

    permission_classes = [IsFaculty]

    def get(self, request):

        return Response({
            "message": "Welcome Faculty",
            "user": request.user.username
        })


class AdminDashboardView(APIView):

    permission_classes = [IsAdmin]

    def get(self, request):

        return Response({
            "message": "Welcome Admin",
            "user": request.user.username
        })


# User Management APIs

class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserManagementSerializer
    permission_classes = [IsAdmin]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserManagementSerializer
    permission_classes = [IsAdmin]