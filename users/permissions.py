"""Permissions for users app"""
from rest_framework import permissions


class IsTheCandidateOrReadOnly(permissions.BasePermission):
    """Permissions for access to a candidate"""
    def has_object_permission(self, request, view, obj) -> bool:
        """Only allow candidates to modify their profile."""
        if obj.owner == request.user:
            return True
        return request.method in permissions.SAFE_METHODS


class IsRecruiterAndOwner(permissions.BasePermission):
    """Permissions for access to a recruiter"""
    def has_object_permission(self, request, view, obj) -> bool:
        """Only allow recruiters to access and modify their profile."""
        return (request.user.is_authenticated
                and hasattr(request.user, "recruiter")
                and request.user.recruiter == obj)
