from django.shortcuts import render, get_object_or_404
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework import generics
from rest_framework import serializers
from .serializers import *
from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes


from rest_framework import generics
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = serializer.instance
        access = AccessToken.for_user(user)
        data = {
            'access': str(access),

        }
       
        return Response(data, status=HTTP_201_CREATED, headers=headers)

# --------------------------création des shops---------------------
class ShopSerializer(serializers.Serializer):
    fullname_shops = serializers.CharField()
    nombre_employes = serializers.CharField()
    detailed_location = serializers.CharField()
    phone_shops = serializers.CharField()
    office_address_acheteurs = serializers.CharField()
    home_address_acheteurs = serializers.CharField()
    categorie = serializers.CharField()
    
    


# -------------------------requests--------------------

    

@api_view(["GET"])
def get_categorie(request):
    data = Categorie.objects.order_by("?")
    serializer = SerialCategorie(data, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_requetes(request):
    data = Requetes.objects.order_by('?')
    serializer = SerialRequest(data, many=True)
    return Response(serializer.data)





class requestSerializer(serializers.Serializer):
    produit = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField()
    quantite = serializers.IntegerField()
    prix = serializers.IntegerField()
    satisfaite = serializers.BooleanField()
    nouveau_prix = serializers.IntegerField()
    nombre_vues = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def CreateRequete(request):
    serializer = requestSerializer(data=request.data)
    if serializer.is_valid():
        acheteur = request.user
        data = Requetes(acheteur = acheteur, **serializer.validated_data)
        data.save()
        return Response({"message": "réussi"})
    return Response(Exception)

# --------------------créer un vendeur-----------------

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ValideBoutique(request):
    serializer = CreateBoutique(data=request.data)
    if serializer.is_valid():
        proprio = request.user
        serializer.save(proprio = proprio)
        return Response(f"C'est bon, c'est créer {str(proprio)}")
    return Response(Exception)
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ValideRequetes(request):
    serializer = SerialRequest(data=request.data)
    if serializer.is_valid():
        acheteur = request.user
        serializer.save(acheteur = acheteur)
        return Response(f"C'est bon, c'est créer {str(acheteur)}")
    return Response(Exception)
    