from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomerUserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id:
            return True
