# Generated by Django 3.1.2 on 2020-10-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_device_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='gas_status',
            field=models.BooleanField(default=True),
        ),
    ]