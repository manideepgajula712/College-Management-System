from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):

    serializer_class = AttendanceSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "STUDENT":
            return Attendance.objects.filter(
                student__user=user
            )

        return Attendance.objects.all()
