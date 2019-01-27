from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, default = 'No Question')
    pub_date = models.DateTimeField('date published', auto_now = False)
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    queston = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text