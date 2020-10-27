from django.shortcuts import render, HttpResponse, redirect 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Device
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required(login_url="/accounts/login")
def panel_views(request):

    return render(request, 'panel/panel.html')

@csrf_exempt
def degree_views(request):
    form=request.POST.get(params)
    print(form)
    device = Device.objects.get(id=1)
    if form.is_valid() : 
        form = form.cleaned_data()
        Device.degree = form
    device.save()
    return HttpResponse()

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
    return HttpResponse()

def gas_views(request):
    device = Device.objects.get(id=1) 
    status = device.gas_status
    if status == True :  
        print(status)
        status = { True                                                                                                                                                                                                                                                                                                                                                                                                                }
    elif status == False : 
        device.window_status = not device.window_status
        print(status)
        status = { False }
    device.save()
    return render(request,'panel/panel.html',{'status':status})
def window_views (request): 
    device = Device.objects.get(id=1)
    device.window_status = not device.window_status
    device.save()
    return HttpResponse()