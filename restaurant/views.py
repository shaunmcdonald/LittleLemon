from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets, filters
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


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = CustomPagination
    search_fields = ['name', 'booking_date']
    ordering_fields = ['name', 'booking_date']
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete']


def index(request):
    return render(request, 'index.html', {})