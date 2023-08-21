from rest_framework import serializers
from .models import Organization
from user.serializers import UserSerializer
from django.utils.translation import gettext_lazy as _

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

class CreateOrganizationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Name'))
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True, label=_('Description'))

    class Meta:
        model = Organization
        fields = ['name', 'description']

class UpdateOrganizationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Name'))
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True, label=_('Description'))