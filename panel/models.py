from django.db import models

# Create your models here.
class Device(models.Model):
    status = models.BooleanField(default=True)
    status2 = models.BooleanField(default=True)
    status3 = models.BooleanField(default=True)
