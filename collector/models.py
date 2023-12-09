# app/models.py
from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    or_number = models.CharField(max_length=50)
    new_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
