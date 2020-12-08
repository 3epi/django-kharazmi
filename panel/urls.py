from django.urls import path
from . import views 

app_name = 'panel'
urlpatterns = [
    path('panel', views.panel_views , name = 'panel'),
    path('light1', views.light1_views , name = 'light'),
    path('light2', views.light2_views , name = 'light'),
    path('light3', views.light3_views , name = 'light'),
    path('light4', views.light4_views , name = 'light'),
    path('electricity', views.electricity_views , name = 'electricity'),
    path('degree',views.degree_views,name='degree'),
    path('gas',views.gas_views, name = 'gas'),
]
