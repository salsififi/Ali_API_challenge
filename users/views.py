from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from users.models import Candidate, Recruiter
from users.permissions import IsTheCandidateOrReadOnly, IsRecruiterAndOwner
from users.serializers import CandidateSerializer, RecruiterSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing candidates."""
    serializer_class = CandidateSerializer
    permission_classes = (IsTheCandidateOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        """All active candidates are returned"""
        return Candidate.objects.filter(user__is_active=True)


class RecruiterViewSet(viewsets.ModelViewSet):
    """ViewSet for recruiters"""
    serializer_class = RecruiterSerializer
    permission_classes = (IsRecruiterAndOwner,)

    def get_queryset(self) -> QuerySet:
        """Returns only user's recruiter data"""
        return Recruiter.objects.filter(user=self.request.user)

    def get_object(self):
        """Override pour vérifier que l'utilisateur n'accède qu'à ses propres données."""
        obj = super().get_object()  # Récupère l'objet basé sur l'ID de l'URL
        if obj.user != self.request.user:
            raise PermissionDenied("Vous n'avez pas la permission d'accéder à cette ressource.")
        return obj

    def list(self, request, *args, **kwargs):
        """Prevent listing recruiters"""
        return Response([], status=status.HTTP_204_NO_CONTENT)

