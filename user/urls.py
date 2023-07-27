from django.urls import path, include
from .views import (
    CreateUserAccountView,
    LoginUserView,
    FacebookLogin, 
    GoogleLogin,
    PasswordConfirmationView
)

# app_name = 'user'

urlpatterns = [
    path('auth/register/', CreateUserAccountView.as_view(), name='email_auth_register'),
    path('auth/login/', LoginUserView.as_view(), name='login_user'),

    path('auth/google', GoogleLogin.as_view(), name='google_auth'),
    path('auth/facebook', FacebookLogin.as_view(), name='facebook_auth'),

    path('password/confirm/', PasswordConfirmationView.as_view(), name='password_confirmation'),
]
