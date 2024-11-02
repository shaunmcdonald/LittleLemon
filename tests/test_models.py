# test_models.py
from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import date

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pizza",
            price=Decimal("15.99"),
            inventory=50
        )
    
    def test_get_item(self):
        """Test the get_item method returns correct string representation"""
        self.assertEqual(
            self.menu_item.get_item(),
            "Pizza : 15.99"
        )
        
    def test_title_max_length(self):
        """Test title field max length"""
        max_length = self.menu_item._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)
        
    def test_price_decimal_places(self):
        """Test price field decimal places"""
        decimal_places = self.menu_item._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)
        
    def test_str_method(self):
        """Test string representation of the model"""
        self.assertEqual(str(self.menu_item), "Pizza")

class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=date.today()
        )
    
    def test_get_item(self):
        """Test the get_item method returns correct string representation"""
        expected = f"{self.booking.booking_date} : {self.booking.name}"
        self.assertEqual(self.booking.get_item(), expected)
        
    def test_name_max_length(self):
        """Test name field max length"""
        max_length = self.booking._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
        
    def test_str_method(self):
        """Test string representation of the model"""
        self.assertEqual(str(self.booking), self.booking.name)