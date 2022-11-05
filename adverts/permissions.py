from rest_framework import permissions


class AutherALLStaffOrReadOnly(permissions.BasePermission):
    """
        Just auther and admins can change advert
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.phoneNumber == request.user.phoneNumber:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True


