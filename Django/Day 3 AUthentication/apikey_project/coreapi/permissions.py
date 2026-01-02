from rest_framework.permissions import BasePermission
from coreapi.models import UserProfile


class IsEditorUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            profile = UserProfile.objects.get(user=request.user)
            return profile.role == 'Editor'
        except UserProfile.DoesNotExist:
            return False
