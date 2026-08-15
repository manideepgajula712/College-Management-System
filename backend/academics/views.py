from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer

    permission_classes = [
        IsAuthenticated
    ]


class SubjectViewSet(viewsets.ModelViewSet):

    queryset = Subject.objects.all()

    serializer_class = SubjectSerializer

    permission_classes = [
        IsAuthenticated
    ]