from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [    
    path('', views.IndexView.as_view(), name='index'),
    path('open/', views.OpenView.as_view(), name='open'),
    path('join/', views.JoinView.as_view(), name='join'),
    path('<int:pk>/talk/', views.TalkView.as_view(), name='talk'),
]