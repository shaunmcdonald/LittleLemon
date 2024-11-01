from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('menu', views.MenuViewSet, basename='menu')
router.register('booking/tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='home'),
    path('', include(router.urls)),
]