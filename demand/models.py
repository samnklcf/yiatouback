from django.db import models
from user.models import User
import uuid

from .constant import (
    STATUS
)

class Demand(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    product_name = models.CharField(max_length=200, blank=False)
    slug = models.CharField(max_length=200, blank=False)
    price = models.CharField(max_length=200, blank=True, null=True)
    new_price = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True, blank=True, default='pending')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='demand/', blank=True, null=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="user_demands", 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.product_name
        
    class Meta:
        verbose_name = "Demand"
        indexes = [
            models.Index(fields=['product_name', 'slug']),
            models.Index(fields=['price', 'new_price']),
            models.Index(fields=['description']),
        ]

class Message(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    message = models.TextField(blank=True, null=True)
    demand = models.ForeignKey(
        Demand, 
        on_delete=models.CASCADE, 
        related_name="demand_messages", 
        null=True, 
        blank=True
    )
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="sender_user_messages", 
        null=True, 
        blank=True
    )
    receiver = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="receiver_user_messages", 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 