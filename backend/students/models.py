from django.db import models
from authentication.models import User


class Student(models.Model):

    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    address = models.TextField()

    admission_date = models.DateField()

    department = models.CharField(
        max_length=100
    )

    course = models.CharField(
        max_length=100
    )

    semester = models.PositiveIntegerField()

    guardian_name = models.CharField(
        max_length=100
    )

    guardian_phone = models.CharField(
        max_length=15
    )

    emergency_contact = models.CharField(
        max_length=15
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.student_id} - {self.user.username}"