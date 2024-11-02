# test_forms.py
from django.test import TestCase
from restaurant.forms import BookingForm
from datetime import date, timedelta

class BookingFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'John Doe',
            'no_of_guests': 4,
            'booking_date': date.today() + timedelta(days=1)
        }
    
    def test_valid_form(self):
        """Test form with valid data"""
        form = BookingForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_past_date(self):
        """Test form with past date"""
        past_data = self.valid_data.copy()
        past_data['booking_date'] = date.today() - timedelta(days=1)
        form = BookingForm(data=past_data)
        self.assertFalse(form.is_valid())
        self.assertIn('booking_date', form.errors)
        self.assertEqual(
            form.errors['booking_date'][0],
            "You cannot book a date in the past!"
        )
        
    def test_invalid_guest_number_min(self):
        """Test form with less than minimum guests"""
        invalid_data = self.valid_data.copy()
        invalid_data['no_of_guests'] = 0
        form = BookingForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('no_of_guests', form.errors)
        
    def test_invalid_guest_number_max(self):
        """Test form with more than maximum guests"""
        invalid_data = self.valid_data.copy()
        invalid_data['no_of_guests'] = 21
        form = BookingForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('no_of_guests', form.errors)
        
    def test_empty_name(self):
        """Test form with empty name"""
        invalid_data = self.valid_data.copy()
        invalid_data['name'] = ''
        form = BookingForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        
    def test_date_widget_attributes(self):
        """Test date input widget attributes"""
        form = BookingForm()
        widget = form.fields['booking_date'].widget
        self.assertEqual(widget.input_type, 'date')
        self.assertEqual(
            widget.attrs['min'],
            date.today().isoformat()
        )
        
    def test_guests_widget_attributes(self):
        """Test number of guests widget attributes"""
        form = BookingForm()
        widget = form.fields['no_of_guests'].widget
        self.assertEqual(widget.input_type, 'number')
        self.assertEqual(widget.attrs['min'], 1)
        self.assertEqual(widget.attrs['max'], 20)
        
    def test_required_fields(self):
        """Test all fields are required"""
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
        for field in ['name', 'no_of_guests', 'booking_date']:
            self.assertIn(field, form.errors)
            
    def test_meta_fields(self):
        """Test Meta class fields configuration"""
        form = BookingForm()
        self.assertEqual(
            list(form.Meta.fields),
            ['name', 'no_of_guests', 'booking_date']
        )