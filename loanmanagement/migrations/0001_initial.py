# Generated by Django 4.2.7 on 2023-12-02 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='static/images/')),
                ('document', models.FileField(upload_to='static/documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField()),
                ('duration_period', models.DateField()),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanmanagement.person')),
            ],
        ),
    ]
