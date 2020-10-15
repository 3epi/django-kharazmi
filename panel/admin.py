from django.contrib import admin
from . import models
from .models import Device

class Deviceadmin(admin.ModelAdmin):
    model = Device
    list_display = ['status' ,'status2','status3','id', ]
admin.site.register(models.Device , Deviceadmin)