from django.shortcuts import render

# Create your views here.
from django.views import generic
from chat import models
from chat import forms

class IndexView(generic.FormView):
    template_name = 'chat/index.html'
    form_class = forms.JoinForm
    
    def get(self, request, *args, **kwargs ):        
        chatrooms = models.Chatroom.objects.all()
        room_list = []
        admin_list = []
        value = None
        if len(chatrooms) > 0:      
            for i in chatrooms:  
                room_list.append( (i.id, f'"{i.title}"') )
#                admin_list.append( models.User.objects.all().get(pk=i.admin_id).nickname )
            value, label = room_list[0]

        form = self.form_class(options=room_list, init=value)
                 
        return render(request, self.template_name, {'form': form, 'admin_list':admin_list, 'room_list':chatrooms})                
        
    def post(self, request, *args, **kwargs ):
        pass

    