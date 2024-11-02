from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import date
from decimal import Decimal
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuTemplateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
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
        
    def test_menu_list_template(self):
        """Test the menu list template view"""
        response = self.client.get(reverse('restaurant:menu-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertIn('menu', response.context)
        
    def test_menu_detail_template(self):
        """Test the menu detail template view"""
        response = self.client.get(
            reverse('restaurant:menu-detail', kwargs={'pk': self.menu1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_item.html')
        self.assertIn('menu_item', response.context)

class MenuAPIViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = APIClient()
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
        
    def test_getall(self):
        """Test retrieving all menu items"""
        response = self.client.get(reverse('restaurant-api:menu-list'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)
        
    def test_create_menu_item_authenticated(self):
        """Test creating a menu item when authenticated"""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Pasta',
            'price': '12.99',
            'inventory': 40
        }
        response = self.client.post(reverse('restaurant-api:menu-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)
        
    def test_menu_detail(self):
        """Test retrieving a specific menu item"""
        response = self.client.get(
            reverse('restaurant-api:menu-detail', kwargs={'pk': self.menu1.pk})
        )
        serializer = MenuSerializer(self.menu1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class BookingTemplateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.booking = Booking.objects.create(
            name='Test User',
            no_of_guests=4,
            booking_date=date.today()
        )
        
    def test_booking_list_authenticated(self):
        """Test booking list view for authenticated users"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('restaurant:booking-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')
        
    def test_booking_list_unauthenticated(self):
        """Test booking list view redirects for unauthenticated users"""
        response = self.client.get(reverse('restaurant:booking-list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, 
            f"{reverse('restaurant:login')}?next={reverse('restaurant:booking-list')}"
        )

class BookingAPIViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = APIClient()
        self.booking = Booking.objects.create(
            name='Test User',
            no_of_guests=4,
            booking_date=date.today()
        )
        
    def test_getall(self):
        """Test retrieving all bookings"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('restaurant-api:booking-list'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)
        
    def test_create_booking_authenticated(self):
        """Test creating a booking when authenticated"""
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'New User',
            'no_of_guests': 2,
            'booking_date': date.today().isoformat()
        }
        response = self.client.post(reverse('restaurant-api:booking-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
        
    def test_booking_detail(self):
        """Test retrieving a specific booking"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('restaurant-api:booking-detail', kwargs={'pk': self.booking.pk})
        )
        serializer = BookingSerializer(self.booking)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_booking_unauthenticated(self):
        """Test creating a booking when not authenticated"""
        data = {
            'name': 'New User',
            'no_of_guests': 2,
            'booking_date': date.today().isoformat()
        }
        response = self.client.post(reverse('restaurant-api:booking-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)