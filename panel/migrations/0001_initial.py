# Generated by Django 3.1.2 on 2020-10-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('light_status', models.BooleanField(default=True)),
                ('electricity_status', models.BooleanField(default=True)),
                ('auto_manual_status', models.BooleanField(default=True)),
            ],
        ),
    ]
