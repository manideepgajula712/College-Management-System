from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User, Role


class AuthenticationTests(APITestCase):

    def setUp(self):

        self.student_role = Role.objects.create(name="STUDENT")
        self.admin_role = Role.objects.create(name="COLLEGE_ADMIN")

        self.student = User.objects.create_user(
            username="student_test",
            email="student@test.com",
            password="Student@123",
            role=self.student_role
        )

        self.admin = User.objects.create_user(
            username="admin_test",
            email="admin@test.com",
            password="Admin@123",
            role=self.admin_role
        )

    def test_registration(self):

        url = reverse("register")

        data = {
            "username": "newstudent",
            "email": "newstudent@test.com",
            "password": "Password@123",
            "role": self.student_role.id
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):

        url = reverse("login")

        data = {
            "username": "student_test",
            "password": "Student@123"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_profile(self):

        login = self.client.post(
            reverse("login"),
            {
                "username": "student_test",
                "password": "Student@123"
            }
        )

        token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_dashboard(self):

        login = self.client.post(
            reverse("login"),
            {
                "username": "student_test",
                "password": "Student@123"
            }
        )

        token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        response = self.client.get(reverse("student-dashboard"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_dashboard(self):

        login = self.client.post(
            reverse("login"),
            {
                "username": "admin_test",
                "password": "Admin@123"
            }
        )

        token = login.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

        response = self.client.get(reverse("admin-dashboard"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)