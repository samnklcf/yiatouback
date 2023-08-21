from rest_framework import serializers
from .models import (
    Demand, Message
)
from user.serializers import UserSerializer
from django.utils.translation import gettext_lazy as _

from .constant import (
    STATUS
)

class DemandSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Demand()
        fields = [
            'id',
            'product_name',
            'price',
            'new_price',
            'status',
            'description',
            'image',
            'user',
        ]

    def __init__(self, *args, user=False, **kwargs):
        if user != True:
            self.fields.pop('user')

        return super().__init__(*args, **kwargs)
    
class MessageSerializer(serializers.ModelSerializer):
    demand = DemandSerializer()
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = [
            'id',
            'message',
            'demand',
            'sender',
            'receiver'
        ]

    def __init__(self, *args, demand=False, sender=False, receiver=False, **kwargs):
        if demand != True:
            self.fields.pop('demand')
        
        if sender != True:
            self.fields.pop('sender')

        if receiver != True:
            self.fields.pop('receiver')

        return super().__init__(*args, **kwargs)

class CreateDemandSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Product Name'))
    price = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Price'))
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True, label=_('Description'))
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Demand
        fields = ['product_name', 'price', 'description', 'image']

class GetDemandListSerializer(serializers.Serializer):
    status = serializers.ChoiceField(required=False, allow_blank=True, allow_null=True, choices=STATUS)

class UpdateDemandSerializer(serializers.Serializer):
    product_name = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Product Name'))
    price = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Price'))
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True, label=_('Description'))
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

class ChangeDemandStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(required=False, allow_blank=True, allow_null=True, choices=STATUS)

class CreateMessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True, allow_blank=False, allow_null=False, label=_('Message'))

    class Meta:
        model = Message
        fields = ['message']