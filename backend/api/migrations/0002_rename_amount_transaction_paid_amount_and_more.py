# Generated by Django 4.0.10 on 2023-11-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='paid_amount',
        ),
        migrations.AddField(
            model_name='student',
            name='bus_number',
            field=models.IntegerField(null=True),
        ),
    ]
