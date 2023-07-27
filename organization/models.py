from django.db import models
from user.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to='organization/banners/', blank=True, null=True)
    logo = models.ImageField(upload_to='organization/logos/', blank=True, null=True)

    def __str__(self):
        return self.name
