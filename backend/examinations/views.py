from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Examination, Result
from .serializers import ExaminationSerializer, ResultSerializer


class ExaminationViewSet(viewsets.ModelViewSet):

    serializer_class = ExaminationSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "STUDENT":
            try:
                student = user.student_profile

                return Examination.objects.filter(
                    course__course_name=student.course
                )

            except Exception:
                return Examination.objects.none()

        return Examination.objects.all()


class ResultViewSet(viewsets.ModelViewSet):

    serializer_class = ResultSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role and user.role.name == "STUDENT":
            return Result.objects.filter(
                student__user=user
            )

        return Result.objects.all()
