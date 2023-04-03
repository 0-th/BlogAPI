from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # allow GET, HEAD, OPTIONS request. enables read permissions only
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed if user making the request
        # is an authro
        return obj.author == request.user
