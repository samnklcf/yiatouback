from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from api.models import Liste
from .serializers import serialisatio
from django.contrib.auth.decorators import login_required
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
import os
import asyncio
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

import datetime


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





    



@api_view(["POST"])
def creer(request):
    dates= datetime.datetime.now()
    if request.method =="POST":
        
        
        nom = request.POST['nom']
        
        donne = Liste(nom = nom, Prix = dates)
        donne.save()

    return Response('reussit')
# --------------------------modifié--------------------



    


    
