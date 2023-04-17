"""traduirePdf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('creation-2f416677-858f-796a-a221-690e5e4ae75a2f416677-858f-796a-a221-690e5e4ae75a', UserCreateView.as_view(), name='user-create'),
    path("api/", include('api.urls')),
    path("categorie/", get_categorie, name=""),
    path("data/corrections", get_corrections, name=""),
    path("data/documents", get_documents, name=""),
    path("data/blog", get_blog, name=""),
    path("data/marketing/<int:pk>", get_one),
    path("create-shop/",shop),
    path("create-request/",Requete),
    path('sam/', include('rest_framework.urls')),
    
    
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
