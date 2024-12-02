"""Views for jobs app"""
from django.db.models import QuerySet
from rest_framework import viewsets

from jobs import permissions
from jobs.models import JobOffer
from jobs.serializers import JobOfferSerializer


class PublicJobOfferViewSet(viewsets.ModelViewSet):
    """ViewSet for public published job offers"""
    serializer_class = JobOfferSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        """Only published job offers are returned"""
        return JobOffer.objects.filter(published=True)


class PrivateJobOfferViewSet(viewsets.ModelViewSet):
    """ViewSet for private access to one's job offers"""
    serializer_class = JobOfferSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)

    def get_queryset(self) -> QuerySet:
        """All user job offers are returned"""
        return JobOffer.objects.filter(owner=self.request.user)
