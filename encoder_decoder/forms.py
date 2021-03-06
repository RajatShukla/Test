from registration.backends import default

__author__ = 'RAJAT'
from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))



class Base64EncoderForm(forms.Form):

    """
    This class creates the form of base64 encoder utility
    """
    error_css_class = 'error'
    error_css_class = 'error'
    required_css_class = 'required'

    codecTypes = (('1','UTF-16'), ('2','UTF-32'), ('3','UTF-8'),
                  ('4','ASCII'), ('5','CP1256'), ('6','ISO-8859-1'),
                  ('7','ISO-8859-2'), ('8','ISO-8859-6'), ('9','ISO-8859-15'),
                  ('10','Windows-1252'))

    inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 75, 'placeholder': 'Please enter the  input text',}) ,
                                max_length=600, label=_("Input Text "), required=True,)
    #choiceFields = forms.ChoiceField(widget=forms.(renderer=HorizontalRadioRenderer), choices=codecTypes, initial='1', required=True)
    choiceFields = forms.ChoiceField(choices=codecTypes, initial='1', required=True, label=_("Encoding Types"))

    class Meta:
        pass
        #model = Base64Form
        fields = ('Input Text', 'Choice Fields')



class Base64DecoderForm(forms.Form):

    """
    This class creates the form of base64 decoder utility

    """
    codecTypes = (('1','UTF-16'), ('2','UTF-32'), ('3','UTF-8'),
                  ('4','ASCII'), ('5','CP1256'), ('6','ISO-8859-1'),
                  ('7','ISO-8859-2'), ('8','ISO-8859-6'), ('9','ISO-8859-15'),
                  ('10','Windows-1252'))
    #inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="base64 string")
    inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder': 'Please enter the  input text',}) ,
                                max_length=600, label=_("Input Text "), required=True,)
    #choiceFields = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), choices=codecTypes, initial='1', required=True)
    choiceFields = forms.ChoiceField(choices=codecTypes, initial='1', required=True, label=_("Decoding Types"))

    class Meta:
        #model = Base64Form
        fields = ('Input Text',  'Choice Fields')

