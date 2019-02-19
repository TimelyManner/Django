from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from chat import models

class ChatChannel(WebsocketConsumer):
    talk_backlog = dict(str())
    
    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_id = 'chat_%s' % self.room_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_id,
            self.channel_name
        )

        self.accept()
        user = models.User.objects.all().get(pk=self.user_id)
        message = f'Welcome~ <b>{user.nickname_text}</b> has joined!'
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def disconnect(self, close_code):
        # Leave room group
        user = models.User.objects.all().get(pk=self.user_id)
        message = f'Bye~ <b>{user.nickname_text}</b> has left!'
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_id,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json['user']
        user = models.User.objects.all().get(pk=user_id)
        message = f'<b>{user.nickname_text}</b> : {message} '

        try:
            self.talk_backlog[self.room_group_id] = self.talk_backlog[self.room_group_id] + message
        except KeyError:
            self.talk_backlog[self.room_group_id] = ''
            
        print(f'talk = "{self.talk_backlog[self.room_group_id]}"')
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
        
        