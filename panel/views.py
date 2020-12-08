from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect 
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Device
from django.views.decorators.csrf import csrf_exempt
import requests

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

def light1_views(request):
    response = requests.get('https://kharazmi23.herokuapp.com/api/status/lamps')
    result = response.json()
    if result[1]["state"] == '0' : 
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=1&state=1')
    elif result[1]["state"] == '1' :
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=1&state=0')
    print (result)
    return HttpResponse(response)

def light2_views(request):
    response = requests.get('https://kharazmi23.herokuapp.com/api/status/lamps')
    result = response.json()
    if result[2]["state"] == '0' : 
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=2&state=1')
    elif result[2]["state"] == '1' :
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=2&state=0')
    return HttpResponse(response)

def light3_views(request):
    response = requests.get('https://kharazmi23.herokuapp.com/api/status/lamps')
    result = response.json()
    if result[3]["state"] == '0' : 
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=3&state=1')
    elif result[3]["state"] == '1' :
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=3&state=0')
    return HttpResponse(response)

def light4_views(request):
    response = requests.get('https://kharazmi23.herokuapp.com/api/status/lamps')
    result = response.json()
    if result[4]["state"] == '0' : 
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=4&state=1')
    elif result[4]["state"] == '1' :
        requests.get('https://kharazmi23.herokuapp.com/api/dev?id=4&state=0')
    return HttpResponse(response)


def electricity_views(request):
    response = requests.get('https://kharazmi23.herokuapp.com/api/status/lamps')
    result = response.json()
    requests.get('https://kharazmi23.herokuapp.com/api/dev?id=1&state=0')
    requests.get('https://kharazmi23.herokuapp.com/api/dev?id=2&state=0')
    requests.get('https://kharazmi23.herokuapp.com/api/dev?id=3&state=0')
    requests.get('https://kharazmi23.herokuapp.com/api/dev?id=4&state=0')
    return HttpResponse(response)



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
    #return render(request,'panel/panel.html',{'status':status})
    return JsonResponse({'status':'True'})
