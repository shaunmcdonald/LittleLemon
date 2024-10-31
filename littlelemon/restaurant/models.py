from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField(default=0)
    
    # def __str__(self):
    #   return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=0)
    booking_date = models.DateField()

#     def __str__(self): 
#         return self.first_name