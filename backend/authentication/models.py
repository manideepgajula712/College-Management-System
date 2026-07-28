from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    ROLE_CHOICES = (
        ('SUPER_ADMIN', 'Super Admin'),
        ('COLLEGE_ADMIN', 'College Admin'),
        ('PRINCIPAL', 'Principal'),
        ('HOD', 'Head of Department'),
        ('FACULTY', 'Faculty'),
        ('STUDENT', 'Student'),
        ('PARENT', 'Parent'),
        ('ACCOUNTANT', 'Accountant'),
        ('LIBRARIAN', 'Librarian'),
        ('PLACEMENT_OFFICER', 'Placement Officer'),
        ('HOSTEL_WARDEN', 'Hostel Warden'),
        ('TRANSPORT_MANAGER', 'Transport Manager'),
    )

    name = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        unique=True
    )

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='authentication_user_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='authentication_user_permissions',
        blank=True
    )

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username