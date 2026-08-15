from rest_framework import serializers

from .models import Course, Subject


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course

        fields = [
            "id",
            "course_code",
            "course_name",
            "department",
            "duration_years",
            "description",
            "created_at",
            "updated_at",
        ]


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject

        fields = [
            "id",
            "course",
            "subject_code",
            "subject_name",
            "semester",
            "credits",
            "description",
            "created_at",
            "updated_at",
        ]