from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""
    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'password')

class FaceSerializer(serializers.ModelSerializer):
    """Serializer to map the Face Model instance into JSON format."""
    class Meta:
        model = Face
        fields = ('id', 'user', 'shape', 'chin_angle', 'mofa_ratio', 'hlmo_angle')
        read_only_fields = ("created_at", "updated_at")