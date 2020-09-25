from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.home),
    path('panel/', views.panel),
    path('login/', views.login),
    path('signup/', views.signup),
    path('articles/', include('articles.urls'))


]

urlpatterns += staticfiles_urlpatterns()