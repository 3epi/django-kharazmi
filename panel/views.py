from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Device
# Create your views here.


@login_required(login_url="/accounts/login")
def panel_views(request):

    return render(request, 'panel/panel.html')


def light_views(request):
    device = Device.objects.get(id=1)
    device.light_status = not device.light_status
    device.save()
    return HttpResponse()

def electricity_views(request):
    device = Device.objects.get(id=1)
    device.electricity_status = not device.electricity_status
    device.save()
    return HttpResponse()


def manualorauto_views(request):
    device = Device.objects.get(id=1)
    device.auto_manual_status = not device.auto_manual_status
    device.save()
    return redirect()
