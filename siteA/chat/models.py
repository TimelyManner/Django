from django.db import models

# Create your models here.
class Chatroom(models.Model):
    title_text = models.CharField(max_length=20, default='No Title')
    created_date = models.DateTimeField('created_date')        
    
    def __str__(self):
        return self.title_text   

class User(models.Model):
    nickname_text = models.CharField(max_length=20, default='Anonymous')
    created_date = models.DateTimeField('created_date')
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    is_on = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.nickname_text