"""URL configuration for api_challenge project"""
from rest_framework import permissions
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api_challenge import settings
from jobs.views import PublicJobOfferViewSet, PrivateJobOfferViewSet
from users.views import CandidateViewSet, RecruiterViewSet


# API routers
router = DefaultRouter()
router.register(r'job-offers/', PublicJobOfferViewSet, basename='public-job-offers')
router.register(r'candidates/', CandidateViewSet, basename='candidates')
router.register(r'recruiters/', RecruiterViewSet, basename='recruiter')

recruiter_job_offers_router = NestedDefaultRouter(router, 'recruiters/', lookup='recruiter')
recruiter_job_offers_router.register(r'job-offers/', PrivateJobOfferViewSet, basename='private-job-offers')

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        default_version='v0.1',
        description="API for API_challenge project",
        contact=openapi.Contact(email="salsififi@yahoo.fr"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls + recruiter_job_offers_router.urls)),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
