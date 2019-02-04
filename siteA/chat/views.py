from django.shortcuts import render

# Create your views here.
from django.views import generic
from chat import models
from chat import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.core.exceptions import ObjectDoesNotExist 

class ChatInfo:
    title = None
    owner = None
    num_chatters = None
    time = None    

class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'
    
    def get(self, request, *args, **kwargs ):        
        chatrooms = models.Chatroom.objects.all()
        users = models.Chatroom.objects.all()
        chat_list = []
        chat_info = ChatInfo()
        for cr in chatrooms:             
            chat_info.title = cr.title_text            
            chat_info.time = datetime.datetime.now() - cr.created_date.replace(tzinfo=None)
            chatters = models.User.objects.filter(chatroom=cr.id)
            chat_info.num_chatters = len(chatters.all())
            chat_info.owner = chatters.get(is_owner=True)
            chat_list.append(chat_info)
        print(f'chatlist: {chat_list}')                    
        return render(request, self.template_name, {'chat_list':chat_list})     
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
    
class OpenView(generic.TemplateView):
    template_name = 'chat/open.html'

    def get(self, request, *args, **kwargs ):
        return render(request, self.template_name, {})
    
    def post(self, request, *args, **kwargs ):
        theme = request.POST['theme']
        chatroom = None
        if len(request.POST['theme']) > 0 and len(request.POST['nickname']) > 0:
            try:
                chatroom = models.Chatroom.objects.all().get(title_text=theme)
                return HttpResponseRedirect(reverse('chat:talk', args=(None,)))        
            except ObjectDoesNotExist:
                nickname = request.POST['nickname']                                             
                user = models.User(nickname_text=nickname, created_date=datetime.datetime.now())
                chatroom = models.Chatroom(title_text=theme, owner=user, created_date=datetime.datetime.now())
                user.save()                
                chatroom.save()
                return HttpResponseRedirect(reverse('chat:talk', args=(chatroom.id,)))
        else:
            return HttpResponseRedirect(reverse('chat:talk', args=(None,)))
    
class JoinView(generic.TemplateView):
    template_name = 'chat/join.html'
    
class TalkView(generic.TemplateView):
    template_name = 'chat/talk.html'

    def get(self, request, *args, **kwargs ):
        chatroom = models.Chatroom.objects.all().get(pk=kwargs['pk'])
        return render(request, self.template_name, {'chat_room', chatroom})        
    
    def post(self, request, *args, **kwargs ):
        return HttpResponseRedirect(reverse('chat:talk'))