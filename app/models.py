from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    price_per_hour = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    photo = models.URLField(max_length=255)


class ScheduledClass(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='scheduled_classes',
    )
