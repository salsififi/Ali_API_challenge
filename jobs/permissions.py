"""Permissions for jobs app"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permissions for access to a job offer"""
    def has_object_permission(self, request, view, obj) -> bool:
        """Only allow owners of a job offer to edit it."""
        if obj.owner == request.user:
            return True
        return request.method in permissions.SAFE_METHODS
