from django.urls import path
from mypharm import views

app_name = 'mypharm'

urlpatterns = [    
    path('', views.IndexView.as_view(), name='index'),
]