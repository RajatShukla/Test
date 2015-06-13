__author__ = 'RAJAT'
from django import forms
import time

class DateTimeForms(forms.Form):
    input_value = forms.CharField(max_length=100, initial=str(int(time.time())))
    operation_types = (('1','Date Time to Epoch Time'), ('2','Epoch Time to Date Time'))
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=operation_types, initial='1', required=True)
    class Meta:
        fields = ('Inpput Value',  'Operation')
