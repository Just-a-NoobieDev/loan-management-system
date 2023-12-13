# Generated by Django 4.2.7 on 2023-12-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanagement', '0008_alter_loan_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanmanagement.person'),
        ),
    ]