from django.db import models


class Course(models.Model):

    course_code = models.CharField(
        max_length=20,
        unique=True
    )

    course_name = models.CharField(
        max_length=100
    )

    department = models.CharField(
        max_length=100
    )

    duration_years = models.PositiveIntegerField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


class Subject(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    subject_code = models.CharField(
        max_length=20
    )

    subject_name = models.CharField(
        max_length=100
    )

    semester = models.PositiveIntegerField()

    credits = models.PositiveIntegerField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = (
            "course",
            "subject_code",
        )

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"
