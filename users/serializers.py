"""Serializers for users app"""
from rest_framework import serializers

from users.models import CustomUser, Candidate, Recruiter


class _CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for CustomUser model"""
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class _UserRelatedModelSerializer(serializers.ModelSerializer):
    """Generic serializer to handle models related to CustomUser."""
    user = _CustomUserSerializer()

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = _CustomUserSerializer(instance.user, data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CandidateSerializer(_UserRelatedModelSerializer):
    """Serializer for Candidate model"""
    user = _CustomUserSerializer()

    class Meta:
        model = Candidate
        fields = ["user", "work_experiences", "degrees", "applications"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = _CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return Candidate.objects.create(user=user, **validated_data)


class RecruiterSerializer(_UserRelatedModelSerializer):
    """Serializer for Recruiter model"""
    user = _CustomUserSerializer()

    class Meta:
        model = Recruiter
        fields = ["user", "company_name"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = _CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return Recruiter.objects.create(user=user, **validated_data)
