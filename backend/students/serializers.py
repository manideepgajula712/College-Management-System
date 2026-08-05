from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Student

        fields = [
            "id",
            "user",
            "student_id",
            "username",
            "email",
            "date_of_birth",
            "gender",
            "address",
            "admission_date",
            "department",
            "course",
            "semester",
            "guardian_name",
            "guardian_phone",
            "emergency_contact",
            "created_at",
            "updated_at",
        ]