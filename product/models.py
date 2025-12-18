from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255, default='Default Product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name