from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
	return render(request , 'about.html')
def home(request):
	return render(request , 'home.html')
def panel(request):
	return render(request , 'panel.html')
def login(request):
	return render(request , 'login.html')
def signup(request):
	return render(request , 'signup.html')