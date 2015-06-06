from registration.backends import default

__author__ = 'RAJAT'
from django import forms
from encoder_decoder.models import Base64Form

class Base64EncoderForm(forms.Form):

    """
    This class creates the form of base64 encoder utility
    """
    codecTypes = (('1','UTF-16'), ('2','UTF-32'), ('3','UTF-8'),
                  ('4','ASCII'), ('5','CP1256'), ('6','ISO-8859-1'),
                  ('7','ISO-8859-2'), ('8','ISO-8859-6'), ('9','ISO-8859-15'),
                  ('10','Windows-1252'))
    inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Input string")
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=codecTypes, initial='1', required=True)

    class Meta:
        model = Base64Form
        fields = ('Input Text', 'Choice Fields')


class Base64DecoderForm(forms.Form):

    """
    This class creates the form of base64 decoder utility

    """
    codecTypes = (('1','UTF-16'), ('2','UTF-32'), ('3','UTF-8'),
                  ('4','ASCII'), ('5','CP1256'), ('6','ISO-8859-1'),
                  ('7','ISO-8859-2'), ('8','ISO-8859-6'), ('9','ISO-8859-15'),
                  ('10','Windows-1252'))
    inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="base64 string")
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=codecTypes, initial='1', required=True)

    class Meta:
        model = Base64Form
        fields = ('Input Text',  'Choice Fields')

