# Generated by Django 5.1.4 on 2024-12-11 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_sensor_id_measurement_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='created_at',
        ),
    ]
