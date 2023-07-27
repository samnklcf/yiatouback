from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from user.models import User, PasswordResets, UserProfile
from organization.models import Organization
from rest_framework.response import Response

from rest_framework import status
from user.serializers import (
    UserSerializer,
    RegisterUserSerializer,
    LoginUserSerializer,
    PasswordConfirmationSerializer,
    UpdateUserAccountInfosSerializer,
    UpdateUserProfileSerializer,
    ChangePasswordSerializer,
)

from organization.serializers import OrganizationSerializer

from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework_simplejwt.tokens import RefreshToken


class CreateUserAccountView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user)

        user = User.objects.get(email=request.data.get('email'))

        data = {
            "id": user.id,
            "last_name": user.last_name,
            "first_name": user.first_name,
            "email": user.email,
            "username": user.username,
            "is_verified": user.is_verified,
            "is_active": user.is_active,
            "is_organizer": user.is_organizer,
            "profile": UserProfile.objects.filter(user=user).values(
                "about_me",
                "image"
            ),
            "organization": Organization.objects.filter(owner=user).values(
                "id", "name", "logo"
            )
        }

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token),
            'user': data,
        }, status=status.HTTP_201_CREATED)   

class LoginUserView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=request.data.get('email'))

        if not user.check_password(request.data.get('password')):
            return Response({
                "message": "Provided credentials are not correct.",
            }, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken.for_user(user)

        data = {
            "id": user.id,
            "last_name": user.last_name,
            "first_name": user.first_name,
            "email": user.email,
            "username": user.username,
            "is_verified": user.is_verified,
            "is_active": user.is_active,
            "is_organizer": user.is_organizer,
            "profile": UserProfile.objects.filter(user=user).values(
                "about_me",
                "image"
            ),
            "organization": OrganizationSerializer(Organization.objects.filter(owner=user), many=True).data
        }

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token),
            'user': data,
        }, status=status.HTTP_200_OK)
    
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class PasswordConfirmationView(GenericAPIView):
    """ Password confirmation view """
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordConfirmationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "message": "Password confirmed successfully.",
        }, status=status.HTTP_200_OK)
