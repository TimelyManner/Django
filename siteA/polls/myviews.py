from django.views.generic import View, FormView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice

class IndexView(View):
    template_name = 'polls/index.html'
    
    def get(self, request):
        latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
        context = {'latest_question_list':latest_question_list}
        return render(request, self.template_name, context)

class DetailView(View):
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        question_id = kwargs['question_id']
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
  
class VoteView(FormView):
    template_name = 'polls/detail.html'
    
    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExists):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message':"You didn't select a choice.",            
                })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
    
    
class ResultView(View):
    template_name = 'polls/results.html'
    
    def get(self, request, *args, **kwargs):
        question_id = args[0]
        print('--------------------------------------')
        print(args)
        print(kwargs)
        print('--------------------------------------')
        question = get_object_or_404(Question, pk=question_id)
        return render(request, self.template_name, {'question': question})