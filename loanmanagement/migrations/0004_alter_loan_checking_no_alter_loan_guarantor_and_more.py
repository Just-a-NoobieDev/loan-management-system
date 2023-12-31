# Generated by Django 4.2.7 on 2023-12-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanagement', '0003_loan_checking_no_loan_guarantor_loan_interest_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='checking_no',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='guarantor',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(decimal_places=3, max_digits=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_maturity',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='net',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='processing_fee',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
