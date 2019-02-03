from django import forms
from django.forms import widgets

'''
class JoinForm(forms.Form):
    nick_name = forms.CharField()
    chat_title = forms.CharField()
        
    def __init__(self, options, init, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['choices'] = init
        self.fields['choices'] = forms.ChoiceField(widget=widgets.RadioSelect, choices=options, initial = init)
'''
        
