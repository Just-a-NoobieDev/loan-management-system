# Generated by Django 4.2.7 on 2023-12-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanagement', '0012_alter_loan_checking_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(null=True),
        ),
    ]
