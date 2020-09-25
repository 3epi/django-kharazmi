from django.shortcuts import render
from . import models
# Create your views here.

def articles_lists(request):
	articles = models.Article.objects.all().order_by('date')
	args ={'articles':articles} 
	return render(request , 'articles/articleslists.html' ,args)