"""URL configuration for api_challenge project"""
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api_challenge import settings
from jobs.views import PublicJobOfferViewSet, PrivateJobOfferViewSet
from users.views import CandidateViewSet, RecruiterViewSet


# API routers
router = DefaultRouter()
router.register('job-offers/', PublicJobOfferViewSet, basename='public-job-offers')
router.register('candidates/', CandidateViewSet, basename='candidates')
router.register('recruiters/{id}/', RecruiterViewSet, basename='recruiter')

recruiter_job_offers_router = NestedDefaultRouter(router, 'recruiters/{id}/', lookup='recruiter')
recruiter_job_offers_router.register(r'job-offers/', PrivateJobOfferViewSet, basename='private-job-offers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls + recruiter_job_offers_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
