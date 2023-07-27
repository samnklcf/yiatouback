from django.db import models
from user.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, null=True)
    banner = models.ImageField(upload_to='organization/banners/', blank=True, null=True)
    logo = models.ImageField(upload_to='organization/logos/', blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    email = models.EmailField(default='')
    contact = models.CharField(max_length=25, blank=False)
    website = models.CharField(max_length=100, blank=True)
    owner = models.ManyToManyField(User)     
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        owner = self.owner.first()
        if owner is None:
            return 'No user associated with this organization'
        return owner.email


    class Meta:
        verbose_name = "Organization"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['description']),
            models.Index(fields=['email', 'contact']),
        ]
