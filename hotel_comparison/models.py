from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=255)
    platform = models.CharField(max_length=20, choices=[('Booking', 'Booking.com'), ('Agoda', 'Agoda')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(null=True, blank=True)
    url = models.URLField()
    
    def __str__(self):
        return self.hotel_name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    price_booking = models.FloatField(null=True, blank=True)
    price_agoda = models.FloatField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    booking_url = models.URLField(null=True, blank=True)
    agoda_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
