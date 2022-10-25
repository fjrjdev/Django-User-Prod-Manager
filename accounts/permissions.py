from rest_framework import permissions
from utils.valid_keys import is_valid_keys


class isAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if obj.id == request.user.id and not request.data.get('is_active'):
            invalid_keys = {"is_active"}

            is_valid_keys(invalid_keys=invalid_keys, request_data=request.data)

            return True
