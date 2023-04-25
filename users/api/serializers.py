from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор к модели User"""
    class Meta:
        model = User
        fields = '__all__'
