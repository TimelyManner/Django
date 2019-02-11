from django.shortcuts import render

# Create your views here.
from django.views import generic
from mypharm import forms, models

class IndexView(generic.TemplateView):
    template_name = 'mypharm/index.html'
    
    def get(self, request, *args, **kwargs):
        context = None
        return render(request, self.template_name, {'context':context})   
    
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('mypharm:index'))