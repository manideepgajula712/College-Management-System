from django.db import models
from authentication.models import User


class Faculty(models.Model):

    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="faculty_profile"
    )

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    address = models.TextField()

    department = models.CharField(
        max_length=100
    )

    designation = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=150
    )

    joining_date = models.DateField()

    experience_years = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.employee_id} - {self.user.username}"