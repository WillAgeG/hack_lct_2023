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


class ReadOnlyOrCreateUserOrUpdateProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if (
            request.method == "POST"
            and not user.is_authenticated
        ):
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if (
            user
            and user.is_authenticated
            and user.is_superuser
        ):
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user

        if (
            user
            and user.is_authenticated
            and user == obj
            and request.method == "PATCH"
        ):
            return True
        if (
            user
            and user.is_authenticated
            and user.is_superuser
        ):
            return True
