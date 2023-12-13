# Generated by Django 4.2.7 on 2023-12-12 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanagement', '0009_alter_loan_client_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('or_number', models.CharField(max_length=50)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanmanagement.loan')),
            ],
        ),
    ]
