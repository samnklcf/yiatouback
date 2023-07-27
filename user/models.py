from re import I
from django.db import models
from random import randint
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import gettext_lazy as _
import uuid

def generate_code():
    n = 6
    code = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
    return code

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if not password:
            raise ValueError('Superuser must have a password')

        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    last_name = models.CharField(_('last name'), max_length=255, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    username = models.CharField(_('username'), max_length=255, unique=True, null=True)
    is_verified = models.BooleanField(_('verified'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_organizer = models.BooleanField(_('is organizer'), blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

        indexes = [
            models.Index(fields=['email', 'username']),
        ]

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

class UserProfile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    about_me = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class PasswordResets(models.Model):
    email = models.EmailField(max_length=255)
    token = models.TextField()
    code = models.CharField(default=generate_code, max_length=6, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

