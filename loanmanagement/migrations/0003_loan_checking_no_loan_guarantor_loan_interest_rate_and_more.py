# Generated by Django 4.2.7 on 2023-12-08 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanagement', '0002_alter_person_document_alter_person_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='checking_no',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='loan',
            name='guarantor',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='loan',
            name='interest_rate',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_maturity',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='loan',
            name='net',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='loan',
            name='processing_fee',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
