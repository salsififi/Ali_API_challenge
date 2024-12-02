"""Models for jobs app"""

from django.db import models

from users.models import Recruiter


class JobOffer(models.Model):
    """Model for job offers"""
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    working_arrangements = models.CharField(max_length=150, blank=True)
    contract_type = models.CharField(max_length=50, blank=True)
    date_job_start = models.DateField(blank=True, null=True)
    requirements = models.JSONField(default=list, blank=True, null=True)
    location = models.JSONField(default=dict, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(to=Recruiter,
                              on_delete=models.CASCADE,
                              related_name='joboffers')
    