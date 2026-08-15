from rest_framework.permissions import BasePermission


class IsCollegeAdminOrReadOnly(BasePermission):
    """
    College Admin and Super Admin can perform CRUD.
    Other authenticated users can only read.
    """

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return (
            request.user.role
            and request.user.role.name in [
                "SUPER_ADMIN",
                "COLLEGE_ADMIN",
            ]
        )