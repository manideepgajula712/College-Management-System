from rest_framework import serializers

from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

    student_id = serializers.CharField(
        source="student.student_id",
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

    class Meta:
        model = Attendance

        fields = [
            "id",
            "student",
            "student_id",
            "subject",
            "subject_code",
            "subject_name",
            "date",
            "status",
            "remarks",
            "created_at",
            "updated_at",
        ]