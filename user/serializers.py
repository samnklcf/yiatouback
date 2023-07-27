from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import User, PasswordResets, UserProfile
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class RegisterUserSerializer(ModelSerializer):
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True, label=_('Last name'))
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True, label=_('First name'))
    email = serializers.EmailField(required=True, label=_('email address'))
    username = serializers.CharField(required=False, allow_blank=True, label=_('username'))
    password = serializers.CharField(write_only=True, label=_('password'))
    password2 = serializers.CharField(write_only=True, label=_('confirm password'))
    is_organizer = serializers.BooleanField(required=False, allow_null=True)
    organization_name = serializers.CharField(required=False, label=_('Organization name'), allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'last_name', 'first_name', 'email', 'username', 'password', 'password2', 'is_organizer', 'organization_name']
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}

    def validate(self, data):
        
        # Check if the user is not a organizer then not allow to create an account with the same email
        if User.objects.filter(email=data['email']).exists() and data['is_organizer'] is False:
            raise serializers.ValidationError("User with that email address already exists.")
        
        # Check if the user is a organizer then not allow to create an account with the same email
        elif User.objects.filter(email=data['email'], is_organizer=True).exists():
            raise serializers.ValidationError("User with that email address already exists.")
        
        return data

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be at least %s characters." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get('password')

        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be at least %s characters." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )

        if password != value:
            raise serializers.ValidationError("Passwords doesn't match.")

        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("User with that username already exists.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(
            last_name=validated_data.get('last_name', None),
            first_name=validated_data.get('first_name', None),
            email=validated_data.get('email', None), 
            username=validated_data.get('username', None),
            is_organizer=validated_data.get('is_organizer', None),
        )
        
        if password is not None:
            user.set_password(password)

        # this part will check if the user already exists or not
        try:
            user.save()
        except IntegrityError as e:
            existing_user = User.objects.get(email=user.email)
            # if the user already exists then update the is_organizer (We are in the cas that it's a organizer)
            if existing_user.id:
                user = existing_user
                user.is_organizer = validated_data.get('is_organizer', None)
                user.save()

        if validated_data.get('is_organizer') is True:
            name = validated_data.get('organization_name')
            type = OrganizationType.objects.get(pk=validated_data.get('organization_type'))
            organization = Organization.objects.create(name=name, type=type)
            organization.owner.add(user)

        return user