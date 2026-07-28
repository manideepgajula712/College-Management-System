from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "phone",
            "role",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            phone=validated_data.get("phone"),
            role=validated_data.get("role"),
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        data = super().validate(attrs)

        data["username"] = self.user.username
        data["email"] = self.user.email

        if self.user.role:
            data["role"] = self.user.role.name
        else:
            data["role"] = None

        return data