from django.shortcuts import render

# Create your views here.

def panel_views(request):

    return render(request, 'panel/panel.html')