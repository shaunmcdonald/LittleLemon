from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
	def test_get_item(self):
		item = Menu.objects.create(title="Nachos", price="8.99", inventory="80")
		itemstr = item.get_item()

		self.assertEqual(itemstr, "Nachos : 8.99")


class BookingTest(TestCase):
	def test_get_item(self):
		item = Booking.objects.create(name="Shuri", no_of_guests="20", booking_date="2024-11-01")
		itemstr = item.get_item()

		self.assertEqual(itemstr, "2024-11-01 : Shuri")