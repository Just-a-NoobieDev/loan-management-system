from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Collector(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=254, null=True, blank=True)

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
    checking_no = models.CharField(max_length=250, null=False, blank=False)
    has_active_loan = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Automatically set has_active_loan to False if loan_balance is zero
        if self.loan_balance == 0:
            self.has_active_loan = False

        super().save(*args, **kwargs)

    def __str__(self):
        status = "Active" if self.has_active_loan else "Inactive"
        return f"{self.client_id.name} (ID: {self.id}, Status: {status})"


class Payment(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(null=True)
    or_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.loan_id}"


class Reports(models.Model):
    type = models.CharField(max_length=50)
    filename = models.CharField(max_length=250)
    filepath = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
