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
    
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def shop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        data = Shops(**serializer.validated_data)
        data.save()
        return Response({"message": "réussi"})
    return Response({"message": "Refusé"})

# -------------------------requests--------------------
class requestSerializer(serializers.Serializer):
    acheteur = serializers.CharField()
    produit = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    quantite = serializers.IntegerField()
    prix = serializers.IntegerField()
    satisfaite = serializers.BooleanField()
    nouveau_prix = serializers.IntegerField()
    nombre_vues = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def Requete(request):
    serializer = requestSerializer(data=request.data)
    if serializer.is_valid():
        data = request(**serializer.validated_data)
        data.save()
        return Response({"message": "réussi"})
    return Response(Exception)

    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_categorie(request):
    data = Categorie.objects.order_by('-nom_categorie')
    serializer = SerialCategorie(data, many=True)
    return Response(serializer.data)

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_corrections(request):
#     user = request.user
#     data = user.marketing_set.all().filter(genre="CORRECTIONS").order_by('-datetime')[:20]
#     serializer = SerialMarket(data, many=True)
#     return Response(serializer.data)

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_blog(request):
#     user = request.user
#     data = user.marketing_set.all().filter(genre="BLOG").order_by('-datetime')[:20]
#     serializer = SerialMarket(data, many=True)
#     return Response(serializer.data)

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_documents(request):
#     user = request.user
#     data = user.marketing_set.all().filter(genre="DOCUMENTS").order_by('-datetime')[:20]
#     # serializer = SerialMarket(data, many=True)
#     return Response(serializer.data)

    
# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_one(request, pk):
#     user = request.user
#     data = get_object_or_404(user.marketing_set.all(), pk=pk)
    
#     serializer = SerialMarket(data, many=False)
#     return Response(serializer.data)

# _________________post/blog_______________________________




