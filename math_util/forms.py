from nose.plugins.plugintest import blankline_separated_blocks

__author__ = 'RAJAT'
from django import forms
from django.utils.translation import gettext_lazy as _

def empty_value_validator(value):
    if value == '':
        raise forms.ValidationError("This field is required")

class NumberForms(forms.Form):
    #input_value = forms.CharField(max_length=100, required=True)
    input_value = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Integer Number',}) ,
                                max_length=15, label=_("Input Number"), required=True,
                                validators=[empty_value_validator])
    #opern_list = ['celing', 'factorial', 'floor', 'frexp']
    #operation = forms.ChoiceField( choices=opern_list)
    operation_types = (('1','Ceiling function'), ('2','Factorial'), ('3','Floor'),
                  ('4','Regular Expression'))
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=operation_types, required=True, label=_("Number Theoretic Operations"))

    class Meta:
        fields = ('Input Number',  'Operation')


class PowLogForms(forms.Form):
    inp_val1 = forms.CharField(max_length=100, required=True, )
    inp_val2 = forms.CharField(max_length=100, required=True)
    operation_types = (('1', 'Power function'), ('2', 'logarithmic Function'))
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=operation_types, initial='1', required=True)
    class Meta:
        fields = ('Value1', 'Value2', 'Operation')



class TrigonmetryForms(forms.Form):
    inp_val1 = forms.CharField(max_length=100, required=True)
    operation_types = (('1', 'arc cosine of x, in radians'), ('2', 'arc sine of x, in radians'),
                       ('3', 'arc tangent of x, in radians'), ('4', 'cosine of x radians'),
                       ('5', 'sine of x radians'), ('6', 'tangent of x radians'))
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=operation_types, initial='1', required=True)
    class Meta:
        fields = ('Value1', 'Operation')


class HyperbolicForms(forms.Form):
    inp_val1 = forms.CharField(max_length=100, required=True, initial=10)
    operation_types = (('1','inverse hyperbolic cosine of x'), ('2', 'inverse hyperbolic sine of x'),
                       ('3', 'inverse hyperbolic tangent of x'), ('4', 'hyperbolic cosine of x'),
                       ('5', 'hyperbolic sine of x' ), ('6', 'hyperbolic tangent of x'))
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=operation_types, required=True, initial=1)
    class Meta:
        fields = ('Value', 'Operation')


class MatrixForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.ncols = kwargs.pop('ncols', 1)
        self.nrows = kwargs.pop('nrows', 1)

        super(MatrixForm, self).__init__(*args, **kwargs)

        for i in range(0,self.ncols):
            for j in range(0,self.nrows):
                field = forms.CharField(label="",max_length=2)
                self.fields['c_' + str(i) + '_' + str(j)] = field







