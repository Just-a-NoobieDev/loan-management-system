from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Loan(models.Model):
    client_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    loan_date = models.DateField()
    duration_period = models.DateField()
    interest_rate = models.DecimalField(max_digits=10, decimal_places=3)
    loan_amount = models.DecimalField(max_digits=100, decimal_places=3)
    loan_maturity = models.DateField()
    guarantor = models.CharField(max_length=250)
    processing_fee = models.DecimalField(max_digits=10, decimal_places=3)
    net = models.DecimalField(max_digits=10, decimal_places=3)
    checking_no = models.DecimalField(max_digits=10, decimal_places=3)