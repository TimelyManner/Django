from django.urls import path
from polls.myviews import *
from polls import views 
from polls import myviews

app_name = 'polls'

''' 
urlpatterns = [    
    path('', IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''

urlpatterns = [    
    path('', myviews.IndexView.as_view(), name='index'),
#    path('<int:pk>/', myviews.ChoiceView.as_view(), name='detail'),
    path('<int:pk>/vote/', myviews.VoteView.as_view(), name='detail'),
    path('<int:pk>/results/', myviews.ResultView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/vote/', myviews.VoteView.as_view(), name='vote'),
]