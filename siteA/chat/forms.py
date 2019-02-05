from django import forms
from django.forms import widgets
from chat import models

class EnterForm(forms.Form):
    input_text = forms.CharField(max_length=80)    
    talk_area = forms.CharField(widget=forms.Textarea(
        attrs={'readonly':'readonly', 'rows':10, 'cols':60}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.initial['talk_area'] = kwargs['initial']['talk_area']            
            self.fields['talk_area'] = forms.CharField(widget=forms.Textarea, max_length=10000)
            self.talk_area = self.fields['talk_area']
        except KeyError:
            pass
        
    def get_data(self):
        if self.is_valid():
            return self.cleaned_data
        return