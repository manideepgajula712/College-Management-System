from django.db import models

from academics.models import Course, Subject
from faculty.models import Faculty


class Timetable(models.Model):

    DAY_CHOICES = (
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="timetable_entries"
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="timetable_entries"
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="timetable_entries"
    )

    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    room = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "day",
            "start_time"
        ]

    def __str__(self):
        return (
            f"{self.course.course_code} - "
            f"{self.subject.subject_code} - "
            f"{self.day}"
        )
