from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        print(**kwargs)
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['polls', 'books', 'chat']
        return context
