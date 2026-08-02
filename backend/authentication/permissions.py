from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to SUPER_ADMIN and COLLEGE_ADMIN users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.name in [
                "SUPER_ADMIN",
                "COLLEGE_ADMIN",
            ]
        )


class IsFaculty(BasePermission):
    """
    Allows access only to FACULTY users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.name == "FACULTY"
        )


class IsStudent(BasePermission):
    """
    Allows access only to STUDENT users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role
            and request.user.role.name == "STUDENT"
        )