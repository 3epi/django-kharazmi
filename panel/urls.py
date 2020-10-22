from django.urls import path
from . import views 

app_name = 'panel'
urlpatterns = [
    path('panel', views.panel_views , name = 'panel'),
     path('light', views.light_views , name = 'light'),
    path('electricity', views.electricity_views , name = 'electricity'),
    path('manualorauto', views.manualorauto_views , name = 'manualorauto'),
    path('degree',views.degree_views,name='degree'),
    path('gas',views.gas_views, name = 'gas'),
]
