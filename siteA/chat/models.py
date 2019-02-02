from django.db import models

# Create your models here.
class User(models.Model):
    nickname_text = models.CharField(max_length=20, default='Anonymous')
    created_date = models.DateTimeField('created_date')
    def __str__(self):
        return self.nickname_text    
    
class Chatroom(models.Model):
    title_text = models.CharField(max_length=20, default='No Title')
    created_date = models.DateTimeField('created_date')
    users = models.ManyToManyField(User, related_name='owner')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)      
    
    def __str__(self):
        return self.title_text   
 