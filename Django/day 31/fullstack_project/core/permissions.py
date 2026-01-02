from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'Editor'
