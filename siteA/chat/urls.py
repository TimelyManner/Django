from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [    
    path('', views.IndexView.as_view(), name='index'),
    path('open/', views.OpenView.as_view(), name='open'),
    path('join/', views.JoinView.as_view(), name='join'),
    path('<str:error_msg>/enter/', views.EnterView.as_view(), name='enter'),    
    path('<int:pk>/<int:chatter_id>/enter/', views.EnterView.as_view(), name='enter'),
    path('<int:pk>/<int:chatter_id>/<str:msg>/enter/', views.EnterView.as_view(), name='enter'),
]