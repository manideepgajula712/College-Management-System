from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Timetable
from .serializers import TimetableSerializer


class TimetableViewSet(viewsets.ModelViewSet):

    serializer_class = TimetableSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "STUDENT":
            try:
                student = user.student_profile

                return Timetable.objects.filter(
                    course__course_name=student.course
                )

            except Exception:
                return Timetable.objects.none()

        return Timetable.objects.all()
