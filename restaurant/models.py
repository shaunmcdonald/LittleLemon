from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField(default=0)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
      return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=0)
    booking_date = models.DateField()
    
    class Meta:
        ordering = ['booking_date', 'name']

    def __str__(self): 
        return self.name
    
    def get_item(self):
        return f'{self.booking_date} : {self.name}'
