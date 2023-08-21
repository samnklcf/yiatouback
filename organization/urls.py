from django.urls import path, include
from .views import (
    CreateOrganizationView,
    GetOrganizationInfosView,
    UpdateOrganizationView
)

# app_name = 'user'

urlpatterns = [
    path('add/', CreateOrganizationView().as_view(), name='add_new_organization'),
    path('<int:id>/details', GetOrganizationInfosView().as_view(), name='get_organization_details'),
    path('<int:id>/update', UpdateOrganizationView().as_view(), name='update_organization_details'),
]
