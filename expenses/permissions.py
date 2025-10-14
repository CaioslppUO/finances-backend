# Django REST
from rest_framework.permissions import BasePermission


class IsInGroup(BasePermission):
    """
    Verify if the user is in a specific group.
    """

    def has_permission(self, request, view):
        required_groups = getattr(view, "required_groups", None)

        # Verify if user is admin
        if request.user.is_superuser:
            return True

        # Bypass if no group is required
        if not required_groups:
            return True

        # Block unauthenticated users
        if not request.user or not request.user.is_authenticated:
            return False

        # Verify user groups
        return request.user.groups.filter(name__in=required_groups).exists()
