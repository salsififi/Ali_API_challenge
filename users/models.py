"""Contains all user models and their managers"""

from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

PROFILES = {
    "CANDIDATE": "candidate",
    "RECRUITER": "recruiter",
}


class CustomUserManager(BaseUserManager):
    """Manager for CustomUser"""
    def create_user(self, email, password, profile, **kwargs):
        if not email:
            raise ValueError("email obligatoire.")
        email = self.normalize_email(email)
        user: AbstractUser = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        if profile == "CANDIDATE":
            Candidate.objects.create(user=user)
        elif profile == "RECRUITER":
            Recruiter.objects.create(user=user)
        else:
            raise ValueError("Profile must be 'candidate' or 'recruiter'.")

        return user

    def create_superuser(self, email, password, profile, **kwargs):
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True
        return self.create_user(email, password, **kwargs)


class CustomUser(AbstractUser):
    """Base model for all users"""
    username = None
    email = models.EmailField(unique=True)
    profile = models.CharField(max_length=30, choices=PROFILES, default=PROFILES["CANDIDATE"])
    phone_number = models.CharField(max_length=15, blank=True)
    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    postal_code = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)  
    documents = models.JSONField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to="users", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Candidate(models.Model):
    """Model for users looking for a job"""
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="candidate")
    work_experiences = models.JSONField(default=list, blank=True, null=True)
    degrees = models.JSONField(default=list, blank=True, null=True)
    applications = models.JSONField(default=list, blank=True, null=True)


class Recruiter(models.Model):
    """Model for users proposing job offers"""
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="recruiter")
    company_name = models.CharField(max_length=150, blank=True)
