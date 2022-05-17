from rest_framework import permissions


class IsAuthorRead(permissions.BasePermission):

    message = 'You cant do it'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
