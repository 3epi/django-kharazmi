from django.urls import path
from . import views 

app_name = 'panel'
urlpatterns = [
    path('panel', views.panel_views , name = 'panel'),
    path('light', views.light_views , name = 'lights'),
    path('electricity', views.electricity_views , name = 'electricity'),
    path('manualorauto', views.manualorauto_views , name = 'manualorauto'),
]
