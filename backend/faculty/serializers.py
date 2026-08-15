from rest_framework import serializers

from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Faculty

        fields = [
            "id",
            "user",
            "employee_id",
            "username",
            "email",
            "date_of_birth",
            "gender",
            "address",
            "department",
            "designation",
            "qualification",
            "joining_date",
            "experience_years",
            "created_at",
            "updated_at",
        ]