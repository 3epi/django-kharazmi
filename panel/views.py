from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url="/accounts/login")
def panel_views(request):

    return render(request, 'panel/panel.html')