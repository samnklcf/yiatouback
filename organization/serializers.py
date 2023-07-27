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
            'email',
            'contact',
            'owner',
        ]

    def __init__(self, *args, owner=False, **kwargs):
        if owner != True:
            self.fields.pop('owner')

        return super().__init__(*args, **kwargs)