from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register('menu', views.MenuViewSet, basename='menu')
router.register('booking/tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('home/', views.index, name='home'),
    # path('api-token-auth/', obtain_auth_token), # Exercise Securing the table booking API said to add this but not required with djoser
    path('', include(router.urls)),
]