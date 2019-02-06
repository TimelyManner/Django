from django import forms
from django.forms import widgets
from chat import models

class EnterForm(forms.Form):
    input_text = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'id':'input_text'}), required=False)
    
    talk_area = forms.CharField(widget=forms.Textarea(
        attrs={'id':'talk_area', 'readonly':'readonly', 'rows':10, 'cols':60}))    

    def get_data(self):
        if self.is_valid():
            return self.cleaned_data
        return