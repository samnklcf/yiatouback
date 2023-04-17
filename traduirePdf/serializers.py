from rest_framework import serializers
from .models import *



class SerialCategorie(serializers.ModelSerializer):
    class Meta:
        model= Categorie
        fields = "__all__"
    

class SerialShop(serializers.ModelSerializer):
    class Meta:
        model= Shops
        fields = "__all__"

class SerialRequest(serializers.ModelSerializer):
    class Meta:
        model= Requetes
        fields = "__all__"        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



