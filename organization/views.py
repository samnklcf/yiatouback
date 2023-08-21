from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from organization.models import Organization
from rest_framework.response import Response

from rest_framework import status

from .serializers import (
    OrganizationSerializer,
    CreateOrganizationSerializer,
    UpdateOrganizationSerializer
)

from rest_framework.permissions import (AllowAny, IsAuthenticated)

class CreateOrganizationView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateOrganizationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        organization = Organization.objects.create(
            name = request.data.get('name', None),
            description = request.data.get('description', None)
        )

        user.is_organizer = 1
        user.save()

        organization.owner.add(user)

        return Response(OrganizationSerializer(organization).data, status=status.HTTP_200_OK)
    
class GetOrganizationInfosView(GenericAPIView):
    
    def get(self, request, id, *args, **kwargs):
        
        organization = Organization.objects.get(pk=id)

        if organization is not None:
            return Response(OrganizationSerializer(organization).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Organization not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateOrganizationView(GenericAPIView):
    """ update Organization view """
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateOrganizationSerializer

    def post(self, request, id,  *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        organization = Organization.objects.get(pk=id)

        if organization is not None:
            organization.name = serializer.data.get('name')
            organization.description = serializer.data.get('description')

            organization.save()

            return Response(OrganizationSerializer(organization).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Organization not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)  