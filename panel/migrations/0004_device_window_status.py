# Generated by Django 3.1.2 on 2020-10-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_device_gas_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='window_status',
            field=models.BooleanField(default=True),
        ),
    ]
