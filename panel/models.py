from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    light_status = models.BooleanField(default=True)
    electricity_status = models.BooleanField(default=True)
    auto_manual_status = models.BooleanField(default=True)
