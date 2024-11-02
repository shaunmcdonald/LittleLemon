from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('accounts/register/', views.registration_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('menu/', views.MenuTemplateViewSet.as_view({'get': 'list'}), name='menu-list'),
    path('menu/<int:pk>/', views.MenuTemplateViewSet.as_view({'get': 'retrieve'}), name='menu-detail'),
    path('booking/tables/', views.BookingTemplateViewSet.as_view({
        'get': 'list',
        'post': 'list'
    }), name='booking-list'),
    path('booking/tables/<int:pk>/', views.BookingTemplateViewSet.as_view({
        'get': 'retrieve',
        'post': 'retrieve',
        'delete': 'destroy'
    }), name='booking-detail'),
]