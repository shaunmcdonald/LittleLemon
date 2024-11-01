from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from restaurant.models import Menu, Booking
from restaurant.views import MenuViewSet, BookingViewSet
from restaurant.serializers import MenuSerializer
from decimal import Decimal

class MenuViewSetTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='test_user',
            password='test@pass123'
        )
        
        # Create some test menu items
        self.menu1 = Menu.objects.create(
            title='Pizza',
            price=Decimal('15.99'),
            inventory=50
        )
        self.menu2 = Menu.objects.create(
            title='Burger',
            price=Decimal('8.99'),
            inventory=30
        )
        
        # Setup the API client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        # Define the endpoint
        self.url = '/restaurant/menu/'
        
    def test_getall(self):
        """Test retrieving the menu"""
        response = self.client.get(self.url)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def tearDown(self):
        """Clean up class objects"""
        User.objects.all().delete()
        Menu.objects.all().delete()