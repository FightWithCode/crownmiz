from rest_framework.permissions import BasePermission
from django.conf import settings

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsSpecialAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        key = request.headers.get('x-api-key')
        if request.method in SAFE_METHODS:
            return True
        elif request.user and key and key == settings.X_API_KEY:
            return True
        else:
            return False
