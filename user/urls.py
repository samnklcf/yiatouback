from django.urls import path, include
from .views import (
    CreateUserAccountView,
    LoginUserView,
    FacebookLogin, 
    GoogleLogin,
    PasswordConfirmationView,
    GetUserInfosView,
    UpdateUserAccountInfosView,
    UpdateUserProfileView,
    ChangePasswordView,
    DeleteUserAccountView
)

# app_name = 'user'

urlpatterns = [
    path('auth/register/', CreateUserAccountView.as_view(), name='email_auth_register'),
    path('auth/login/', LoginUserView.as_view(), name='login_user'),

    path('auth/google', GoogleLogin.as_view(), name='google_auth'),
    path('auth/facebook', FacebookLogin.as_view(), name='facebook_auth'),

    path('password/confirm/', PasswordConfirmationView.as_view(), name='password_confirmation'),
    path('profile/', GetUserInfosView.as_view(), name='user_account_data'),
    path('update-account/', UpdateUserAccountInfosView.as_view(), name='update_user_account_data'),
    path('update-profile/', UpdateUserProfileView.as_view(), name='update_user_profile'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
    path('deactivate-account/', DeleteUserAccountView.as_view(), name='deactivate_account'),
]
