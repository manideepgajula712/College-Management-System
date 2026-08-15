from rest_framework import serializers

from .models import Examination, Result


class ExaminationSerializer(serializers.ModelSerializer):

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

    class Meta:
        model = Examination

        fields = [
            "id",
            "course",
            "course_code",
            "course_name",
            "subject",
            "subject_code",
            "subject_name",
            "exam_name",
            "exam_type",
            "exam_date",
            "start_time",
            "end_time",
            "maximum_marks",
            "room",
            "created_at",
            "updated_at",
        ]


class ResultSerializer(serializers.ModelSerializer):

    student_id = serializers.CharField(
        source="student.student_id",
        read_only=True
    )

    student_name = serializers.CharField(
        source="student.user.username",
        read_only=True
    )

    exam_name = serializers.CharField(
        source="examination.exam_name",
        read_only=True
    )

    subject_code = serializers.CharField(
        source="examination.subject.subject_code",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="examination.subject.subject_name",
        read_only=True
    )

    maximum_marks = serializers.IntegerField(
        source="examination.maximum_marks",
        read_only=True
    )

    class Meta:
        model = Result

        fields = [
            "id",
            "student",
            "student_id",
            "student_name",
            "examination",
            "exam_name",
            "subject_code",
            "subject_name",
            "maximum_marks",
            "marks_obtained",
            "grade",
            "grade_point",
            "result_status",
            "remarks",
            "created_at",
            "updated_at",
        ]