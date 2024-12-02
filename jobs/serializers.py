"""Serializer for jobs app models"""
from rest_framework import serializers

from jobs.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    """Serializer for JobOffer model"""
    class Meta:
        model = JobOffer
        fields = "__all__"
