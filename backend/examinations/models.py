from django.db import models

from academics.models import Course, Subject


class Examination(models.Model):

    EXAM_TYPE_CHOICES = (
        ("MIDTERM", "Midterm"),
        ("FINAL", "Final"),
        ("QUIZ", "Quiz"),
        ("ASSIGNMENT", "Assignment"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="examinations"
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="examinations"
    )

    exam_name = models.CharField(
        max_length=100
    )

    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPE_CHOICES
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    maximum_marks = models.PositiveIntegerField()

    room = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "exam_date",
            "start_time"
        ]

    def __str__(self):
        return (
            f"{self.exam_name} - "
            f"{self.subject.subject_code}"
        )


class Result(models.Model):

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="results"
    )

    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE,
        related_name="results"
    )

    marks_obtained = models.PositiveIntegerField()

    grade = models.CharField(
        max_length=5
    )

    grade_point = models.DecimalField(
        max_digits=3,
        decimal_places=2
    )

    result_status = models.CharField(
        max_length=10,
        choices=(
            ("PASS", "Pass"),
            ("FAIL", "Fail"),
        )
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "student",
            "examination"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["student", "examination"],
                name="unique_student_examination_result"
            )
        ]

    def __str__(self):
        return (
            f"{self.student.student_id} - "
            f"{self.examination.exam_name}"
        )