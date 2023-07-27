from rest_framework import serializers
from .models import Organization
from user.serializers import UserSerializer

class OrganizationSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'description',
            'banner',
            'logo',
            'address',
            'email',
            'contact',
            'owner',
        ]