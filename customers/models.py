# customers/models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
