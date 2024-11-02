from django.shortcuts import render, redirect
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, date
from .forms import BookingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.views.generic import ListView, DetailView


class MenuTemplateViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    renderer_classes = [TemplateHTMLRenderer]
    
    def get_template_names(self):
        if self.action == 'list':
            return ['menu.html']
        elif self.action == 'retrieve':
            return ['menu_item.html']
        return []

    @method_decorator(csrf_protect)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return render(request, 'menu.html', {
            'menu': {'menu': queryset}
        })
    
    @method_decorator(csrf_protect)
    def retrieve(self, request, *args, **kwargs):
        menu_item = self.get_object()
        queryset = self.get_queryset()
        return render(request, 'menu_item.html', {
            'menu_item': menu_item,
            'menu': {'menu': queryset}
        })

# API ViewSet
class MenuAPIViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    renderer_classes = [JSONRenderer]
    search_fields = ['title']
    ordering_fields = ['price', 'title']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]
    
    def destroy(self, request, *args, **kwargs):
        menu_item = self.get_object()
        menu_title = menu_item.title
        self.perform_destroy(menu_item)
        return Response({
            'status': 'success',
            'message': f"Menu item '{menu_title}' has been successfully deleted",
            'auth_method': 'Token' if 'Authorization' in request.headers else 'Session'
        }, status=status.HTTP_200_OK)

class BookingTemplateViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    renderer_classes = [TemplateHTMLRenderer]
    
    def get_template_names(self):
        if self.action == 'list':
            return ['bookings.html']
        return ['book.html']

    @method_decorator(csrf_protect)
    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('restaurant:login')}?next={request.path}")
            
        queryset = self.get_queryset()
        
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save()
                messages.success(request, 'Reservation created successfully!')
                return redirect('restaurant:booking-list')
        
        if request.GET.get('action') == 'create' or request.method == 'POST':
            form = BookingForm(request.POST or None)
            today_bookings = self.get_queryset().filter(booking_date=date.today())
            return render(request, 'book.html', {
                'form': form,
                'bookings': today_bookings,
                'today': date.today()
            })

        return render(request, 'bookings.html', {
            'bookings': queryset
        })

    @method_decorator(csrf_protect)
    def retrieve(self, request, *args, **kwargs):
        if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
            return self.destroy(request, *args, **kwargs)
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(csrf_protect)
    def destroy(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('restaurant:login')}?next={request.path}")
            
        reservation = self.get_object()
        res_date = reservation.booking_date
        person = reservation.name
        
        self.perform_destroy(reservation)
        messages.success(
            request,
            f"Reservation for {person} on {res_date} has been cancelled."
        )
        return redirect('restaurant:booking-list')

class BookingAPIViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer  
    renderer_classes = [JSONRenderer]
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



class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect(reverse('restaurant:booking-list'))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'restaurant:booking-list')
            messages.success(request, f'Welcome back, {username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('restaurant:home')