from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'restaurant-api'

router = DefaultRouter()
router.register('menu', views.MenuAPIViewSet, basename='menu')
router.register('booking/tables', views.BookingAPIViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]