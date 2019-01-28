from django.urls import path
from polls.myviews import *
from polls import views 

app_name = 'polls'
 
urlpatterns = [    
    path('', IndexView.as_view()),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
#    path('<int:question_id>/results/', ResultView.as_view()),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]