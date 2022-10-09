from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    price_per_hour = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    photo = models.URLField(max_length=255)
