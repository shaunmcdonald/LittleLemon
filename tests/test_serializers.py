# test_serializers.py
from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from decimal import Decimal
from datetime import date, timedelta

class MenuSerializerTest(TestCase):
    def setUp(self):
        self.menu_attributes = {
            'title': 'Pizza',
            'price': Decimal('15.99'),
            'inventory': 50
        }
        
        self.menu_item = Menu.objects.create(**self.menu_attributes)
        self.serializer = MenuSerializer(instance=self.menu_item)
    
    def test_contains_expected_fields(self):
        """Test serializer contains all expected fields"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'title', 'price', 'inventory'})
        
    def test_title_field_content(self):
        """Test title field content"""
        data = self.serializer.data
        self.assertEqual(data['title'], self.menu_attributes['title'])
        
    def test_price_field_content(self):
        """Test price field content"""
        data = self.serializer.data
        self.assertEqual(Decimal(data['price']), self.menu_attributes['price'])
        
    def test_inventory_field_content(self):
        """Test inventory field content"""
        data = self.serializer.data
        self.assertEqual(data['inventory'], self.menu_attributes['inventory'])
        
    def test_valid_serializer_data(self):
        """Test serializer with valid data"""
        data = {
            'title': 'Burger',
            'price': '12.99',
            'inventory': 30
        }
        serializer = MenuSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_invalid_price_serializer_data(self):
        """Test serializer with invalid price format"""
        data = {
            'title': 'Burger',
            'price': 'invalid',
            'inventory': 30
        }
        serializer = MenuSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)
        
    def test_invalid_inventory_serializer_data(self):
        """Test serializer with invalid inventory type"""
        data = {
            'title': 'Burger',
            'price': '12.99',
            'inventory': 'invalid'
        }
        serializer = MenuSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('inventory', serializer.errors)

class BookingSerializerTest(TestCase):
    def setUp(self):
        self.booking_attributes = {
            'name': 'John Doe',
            'no_of_guests': 4,
            'booking_date': date.today()
        }
        
        self.booking = Booking.objects.create(**self.booking_attributes)
        self.serializer = BookingSerializer(instance=self.booking)
    
    def test_contains_expected_fields(self):
        """Test serializer contains all expected fields"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'no_of_guests', 'booking_date'})
        
    def test_name_field_content(self):
        """Test name field content"""
        data = self.serializer.data
        self.assertEqual(data['name'], self.booking_attributes['name'])
        
    def test_no_of_guests_content(self):
        """Test no_of_guests field content"""
        data = self.serializer.data
        self.assertEqual(data['no_of_guests'], self.booking_attributes['no_of_guests'])
        
    def test_booking_date_content(self):
        """Test booking_date field content"""
        data = self.serializer.data
        self.assertEqual(data['booking_date'], self.booking_attributes['booking_date'].isoformat())
        
    def test_valid_serializer_data(self):
        """Test serializer with valid data"""
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 2,
            'booking_date': (date.today() + timedelta(days=1)).isoformat()
        }
        serializer = BookingSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_invalid_guests_serializer_data(self):
        """Test serializer with invalid guests number"""
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 'invalid',
            'booking_date': date.today().isoformat()
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('no_of_guests', serializer.errors)
        
    def test_invalid_date_serializer_data(self):
        """Test serializer with invalid date format"""
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 2,
            'booking_date': 'invalid-date'
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('booking_date', serializer.errors)