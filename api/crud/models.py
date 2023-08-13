from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=16, decimal_places=8)
    longitude = models.DecimalField(max_digits=16, decimal_places=8)
    timestamp = models.CharField(max_length=128, blank=True)