from django.shortcuts import render

# Create your views here.
from django.views import generic
from chat import models
from chat import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class IndexView(generic.FormView):
    template_name = 'chat/index.html'
    form_class = forms.JoinForm
    
    def get(self, request, *args, **kwargs ):        
        chatrooms = models.Chatroom.objects.all()
        return render(request, self.template_name, {'room_list':chatrooms})     
        '''        
        room_list=[]        
        value = None
        if len(chatrooms) > 0:      
            for i in chatrooms:  
                room_list.append( (i.id, f'"{i.title_text}"') )
            value, label = room_list[0]
        form = self.form_class(options=room_list, init=value)                
        return render(request, self.template_name, {'form': form, 'room_list':chatrooms})
        '''        
        
    def post(self, request, *args, **kwargs ):
        selected_choice = request.POST['choice']        
        input_name = request.POST['nickname']
        print(f'selected: {selected_choice}, nickname: {input_name}') 
        
        return HttpResponseRedirect(reverse('chat:index'))