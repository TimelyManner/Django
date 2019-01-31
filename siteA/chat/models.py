from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=20, default='Anonymous')
    def __str__(self):
        return self.nickname    
    
class Chatroom(models.Model):
    title = models.CharField(max_length=20, default='No Title')
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_id = models.IntegerField(default=None)      
    
    def __str__(self):
        return self.title