from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication APIs
    path(
        'api/auth/',
        include('authentication.urls')
    ),

    # Password Reset APIs
    path(
        'api/auth/',
        include(
            'django_rest_passwordreset.urls',
            namespace='password_reset'
        )
    ),

    # Student APIs
    path(
        'api/',
        include('students.urls')
    ),

    # Academic APIs
    path(
        'api/academics/',
        include('academics.urls')
    ),

    # Faculty APIs
    path(
        'api/',
        include('faculty.urls')
    ),
        # Attendance APIs
    path(
        'api/',
        include('attendance.urls')
    ),
        # Timetable APIs
    path(
        'api/',
        include('timetable.urls')
    ),
    # Examination APIs
    path(
        'api/',
        include('examinations.urls')
    ),
]