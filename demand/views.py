from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import (
    Demand, Message
)
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.http import Http404
from django.core.paginator import EmptyPage

from .serializers import (
    DemandSerializer,
    CreateDemandSerializer,
    GetDemandListSerializer,
    UpdateDemandSerializer,
    ChangeDemandStatusSerializer,
    CreateMessageSerializer,
    MessageSerializer
)

from rest_framework.permissions import (AllowAny, IsAuthenticated)

class CreateDemandView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateDemandSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        demand = Demand.objects.create(
            product_name = request.data.get('product_name', None),
            price = request.data.get('price', None),
            description = request.data.get('description', None),
            image = request.data.get('image', None),
            user = user
        )

        return Response(DemandSerializer(demand).data, status=status.HTTP_200_OK)
    
class GetDemandListView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetDemandListSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # auth user
        user = request.user

        # get serializer data
        status = serializer.data.get('status')

        demands = Demand.objects.filter(user =user).order_by('price')

        if status is not None:
            demands = demands.filter(status=status)

        try:
            p:PageNumberPagination = self.pagination_class()
            results_list = p.paginate_queryset(demands.distinct(), request)

            serialized_results = DemandSerializer(results_list, many=True)

        except EmptyPage:
                raise Http404
        
        return Response({
            "count": p.page.paginator.count,
            "number_of_pages": p.page.paginator.num_pages,
            "current_page_number": p.get_page_number(request=request, paginator=p),
            "previous_page_link": p.get_previous_link(),
            "next_page_number": p.page.next_page_number() if p.page.has_next() else None,
            "previous_page_number": p.page.previous_page_number() if p.page.has_previous() else None,
            "next_page_link": p.get_next_link(),
            "results": serialized_results.data
        })
    
class GetDemandDetailsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def get(self, request, demand_id, *args, **kwargs):
        """
            GET Detail Demand
        """
        demand = Demand.objects.get(pk=demand_id)

        if demand is not None:
            return Response(DemandSerializer(demand).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Demand not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateDemandView(GenericAPIView):
    """ Update demand view """
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateDemandSerializer

    def post(self, request, demand_id,  *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        demand = Demand.objects.get(pk=demand_id)

        if demand is not None:
            demand.product_name = serializer.data.get('product_name', None)
            demand.price = serializer.data.get('price', None)
            demand.product_name = serializer.data.get('product_name', None)
            demand.image = serializer.data.get('image', None)

            demand.save()

            return Response(DemandSerializer(demand).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Demand not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)
        
class ChangeDemandStatusView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeDemandStatusSerializer

    def post(self, request, demand_id, *args, **kwargs):
        """
            Change demand status
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        demand = Demand.objects.get(pk=demand_id)

        if demand is not None:
            demand.status = serializer.data.get('status', None)
            demand.save()

            return Response(DemandSerializer(demand).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Demand not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)
        
class CreateMessageView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateMessageSerializer

    def post(self, request, demand_id, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        demand = Demand.objects.get(pk=demand_id)

        if demand is not None:
            message = Message.objects.create(
                message = serializer.data.get('message', None),
                demand = demand,
                sender = user
            )

            return Response(MessageSerializer(message).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Demand not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)

class GetDemandMessagesView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

    def get(self, request, demand_id, *args, **kwargs):
        user = request.user

        demand = Demand.objects.get(pk=demand_id)

        if demand is not None:
            messages = Message.objects.filter(demand=demand).order_by('created_at')

            try:
                p:PageNumberPagination = self.pagination_class()
                results_list = p.paginate_queryset(messages.distinct(), request)

                serialized_results = MessageSerializer(results_list, many=True)

            except EmptyPage:
                    raise Http404
            
            return Response({
                "count": p.page.paginator.count,
                "number_of_pages": p.page.paginator.num_pages,
                "current_page_number": p.get_page_number(request=request, paginator=p),
                "previous_page_link": p.get_previous_link(),
                "next_page_number": p.page.next_page_number() if p.page.has_next() else None,
                "previous_page_number": p.page.previous_page_number() if p.page.has_previous() else None,
                "next_page_link": p.get_next_link(),
                "results": serialized_results.data
            })
        
        else:
            return Response({"message": "Demand not found", "code": 404}, status=status.HTTP_404_NOT_FOUND)