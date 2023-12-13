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


class Collector(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name


class Loan(models.Model):
    client_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    loan_date = models.DateField()
    duration_period = models.DateField()
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=100, decimal_places=2)
    loan_maturity = models.DateField()
    guarantor = models.CharField(max_length=250)
    processing_fee = models.DecimalField(max_digits=10, decimal_places=2)
    loan_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    net = models.DecimalField(max_digits=10, decimal_places=2)
    checking_no = models.DecimalField(max_digits=10, decimal_places=0)
    
    def __str__(self):
        return f"{self.client_id.name}"
    
class Payment(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(null=True)
    or_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.loan_id}"

