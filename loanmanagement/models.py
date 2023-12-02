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
