from rest_framework import permissions


class IsUserORALLStaff(permissions.BasePermission):
    """
    Just user and admins can change information
    """
    def has_permission(self, request, view):
        # if request.user.is_authenticated:
        #     return True
        pass

    def has_object_permission(self, request, view, obj):
        if request.user.phoneNumber == obj.phoneNumber:
            return True

        if request.user.email == obj.email:
            return True

        # if request.user.is_superuser:
            # return True



