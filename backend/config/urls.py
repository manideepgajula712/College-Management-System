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
]