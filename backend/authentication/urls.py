from django.urls import path

from .views import (
    UserRegistrationView,
    CustomLoginView,
    ProfileView,
    StudentDashboardView,
    FacultyDashboardView,
    AdminDashboardView,
    UserListView,
    UserDetailView,
)


urlpatterns = [

    # Authentication
    path(
        "register/",
        UserRegistrationView.as_view(),
        name="register"
    ),

    path(
        "login/",
        CustomLoginView.as_view(),
        name="login"
    ),

    path(
        "profile/",
        ProfileView.as_view(),
        name="profile"
    ),


    # Role Dashboards
    path(
        "student-dashboard/",
        StudentDashboardView.as_view(),
        name="student-dashboard"
    ),

    path(
        "faculty-dashboard/",
        FacultyDashboardView.as_view(),
        name="faculty-dashboard"
    ),

    path(
        "admin-dashboard/",
        AdminDashboardView.as_view(),
        name="admin-dashboard"
    ),


    # User Management
    path(
        "users/",
        UserListView.as_view(),
        name="user-list"
    ),

    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
]