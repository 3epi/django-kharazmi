from django.contrib import admin
from . import models
from .models import Device

class Deviceadmin(admin.ModelAdmin):
    model = Device
    list_display = ['name', 'light_status' ,'electricity_status','auto_manual_status','gas_status','window_status','degree','id', ]
admin.site.register(models.Device , Deviceadmin)