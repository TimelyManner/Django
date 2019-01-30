from django.views.generic import View, FormView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from django.views import generic
from django.template.context_processors import request
from polls.forms import VoteForm
from django import forms

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]    

class ChoiceView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get(self, request, *args, **kwargs):
        question = Question.objects.all().get(pk=kwargs['pk'])
        print(f'>>> question_text:{question.question_text}')
        return super().get(request, *args, **kwargs)
  
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    
class VoteView(generic.FormView):
    template_name = 'polls/vote.html'
    form_class = VoteForm
    initial = None
    
    def form_valid(self, form):
        form.vote()
        return super().form_valid()

    def get(self, request, *args, **kwargs):
        question = Question.objects.all().get(pk=kwargs['pk'])
        choices = Choice.objects.filter(queston_id = question.pk)
        choice_list = []
        for c in choices:
            choice_list.append( (c.id, c.choice_text) )
            
        self.choices = tuple(choice_list)
        self.initial = dict( {choice_list[0]} )

        form = self.form_class(options=self.choices, init=self.initial)        
        return render(request, self.template_name, {'form': form,'question':question})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, init = self.initial )
        question = Question.objects.get(pk=kwargs['pk'])
        
        try:        
            selected_choice = Choice.objects.all().get(pk=request.POST.get('choices'))      
        except (KeyError, Choice.DoesNotExists):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message':"You didn't select a choice.",            
                })
        else:
            print(f'>>> selected_choice:{selected_choice.choice_text}')            
            selected_choice.votes += 1
            selected_choice.save() 
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))