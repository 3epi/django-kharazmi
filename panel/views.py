from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Device
# Create your views here.


@login_required(login_url="/accounts/login")
def panel_views(request):

    return render(request, 'panel/panel.html')


def light_views(request):
    print("finally worked")
    Device.objects.all()
    device = Device.objects.get(id=1)
    device.status = not device.status
    device.save()
    return HttpResponse()

def electricity_views(request):
    print("finally worked")
    Device.objects.all()
    device = Device.objects.get(id=1)
    device.status2 = not device.status
    device.save()
    return HttpResponse()


def manualorauto_views(request):
    print("finally worked")
    Device.objects.all()
    device = Device.objects.get(id=1)
    device.status3 = not device.status
    device.save()
    return redirect()
