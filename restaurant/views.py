from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CustomPagination
    search_fields = ['title']
    ordering_fields = ['price', 'title']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    # def get_permissions(self):
    #     if self.request.method != 'GET':
    #         permission_classes = [IsAuthenticated]
    def destroy(self, request, *args, **kwargs):
        menu_item = self.get_object()
        menu_title = menu_item.title
        self.perform_destroy(menu_item)
        
        return Response({
            'status': 'success',
            'message': f"Menu item '{menu_title}' has been successfully deleted",
            'auth_method': 'Token' if 'Authorization' in request.headers else 'Session'
        }, status=status.HTTP_200_OK)


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = CustomPagination
    search_fields = ['name', 'booking_date']
    ordering_fields = ['name', 'booking_date']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()
        res_date = reservation.booking_date
        person = reservation.name
        self.perform_destroy(reservation)
        
        return Response({
            'status': 'success',
            'message': f"Reservation for {person} on {res_date} has been successfully deleted",
            'auth_method': 'Token' if 'Authorization' in request.headers else 'Session'
        }, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'index.html', {})