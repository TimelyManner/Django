from django import forms
from django.forms.widgets import RadioSelect

class VoteForm(forms.Form):
    choices = None
    
    def __init__(self, options, init, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['choices'] = init
        self.fields['choices'] = forms.ChoiceField(widget=RadioSelect,choices=options)