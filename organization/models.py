from django.db import models
from user.models import User
import uuid


class Organization(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to='organization/banners/', blank=True, null=True)
    logo = models.ImageField(upload_to='organization/logos/', blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    owner = models.ManyToManyField(User)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Organization"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['description']),
            models.Index(fields=['email', 'contact']),
        ]
