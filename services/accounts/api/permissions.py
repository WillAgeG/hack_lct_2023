from rest_framework import permissions


class IsAuthenticatedReadOnlyOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == user:
            return True

        if (
            user
            and user.is_authenticated
            and user.is_superuser
        ):
            return True
