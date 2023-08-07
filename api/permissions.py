from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPostOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in SAFE_METHODS:
            return True

        # Allow POST request for all authenticated users
        if request.method == 'POST' and request.user.is_authenticated:
            return True

        # Allow PUT and DELETE requests only for the owner of the post
        return obj.name == request.user