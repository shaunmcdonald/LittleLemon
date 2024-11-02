from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date
from decimal import Decimal

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    inventory = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
      return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    @staticmethod
    def validate_future_date(value):
        if value < date.today():
            raise ValidationError('Booking date cannot be in the past')

    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Number of guests must be at least 1"),
            MaxValueValidator(20, message="Number of guests cannot exceed 20")
        ]
    )
    booking_date = models.DateField(validators=[validate_future_date])
    
    class Meta:
        ordering = ['booking_date', 'name']

    def __str__(self): 
        return self.name
    
    def get_item(self):
        return f'{self.booking_date} : {self.name}'
