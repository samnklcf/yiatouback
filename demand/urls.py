from django.urls import path, include
from .views import (
    CreateDemandView,
    GetDemandListView,
    GetDemandDetailsView,
    UpdateDemandView,
    ChangeDemandStatusView,
    CreateMessageView,
    GetDemandMessagesView
)

# app_name = 'user'

urlpatterns = [
    path('add/', CreateDemandView().as_view(), name='add_new_demand'),
    path('', GetDemandListView().as_view(), name='get_demand_list'),
    path('<int:demand_id>/details', GetDemandDetailsView().as_view(), name='get_demand_details'),
    path('<int:demand_id>/update', UpdateDemandView().as_view(), name='update_demand_details'),
    path('<int:demand_id>/change-status', ChangeDemandStatusView().as_view(), name='change_demand_status'),
    path('<int:demand_id>/add-message', CreateMessageView().as_view(), name='add_demand_message'),
    path('<int:demand_id>/messages', GetDemandMessagesView().as_view(), name='get_demand_messages'),
]
