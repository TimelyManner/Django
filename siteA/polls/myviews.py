from django.views.generic import View, FormView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from django.views import generic
from django.template.context_processors import request

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]    

class ChoiceView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
  
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'