from django.urls import path, include
from .views import (
    CreateUserAccountView,
    LoginUserView,
)

# app_name = 'user'

urlpatterns = [
    path('auth/register/', CreateUserAccountView.as_view(), name='email_auth_register'),
    path('auth/login/', LoginUserView.as_view(), name='login_user'),
]
