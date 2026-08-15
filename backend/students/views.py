from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer
from .permissions import IsCollegeAdminOrReadOnly


class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializer

    permission_classes = [
        IsCollegeAdminOrReadOnly
    ]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if user.role and user.role.name == "STUDENT":
                return Student.objects.filter(
                    user=user
                )

        return Student.objects.all()
