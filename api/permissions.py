from rest_framework.permissions import SAFE_METHODS, BasePermission

from api.models import Follow


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    obj.author == request.user)
