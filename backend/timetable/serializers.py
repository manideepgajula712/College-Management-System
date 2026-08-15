from rest_framework import serializers

from .models import Timetable


class TimetableSerializer(serializers.ModelSerializer):

    course_code = serializers.CharField(
        source="course.course_code",
        read_only=True
    )

    course_name = serializers.CharField(
        source="course.course_name",
        read_only=True
    )

    subject_code = serializers.CharField(
        source="subject.subject_code",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="subject.subject_name",
        read_only=True
    )

    faculty_name = serializers.CharField(
        source="faculty.user.username",
        read_only=True
    )

    class Meta:
        model = Timetable

        fields = [
            "id",
            "course",
            "course_code",
            "course_name",
            "subject",
            "subject_code",
            "subject_name",
            "faculty",
            "faculty_name",
            "day",
            "start_time",
            "end_time",
            "room",
            "created_at",
            "updated_at",
        ]