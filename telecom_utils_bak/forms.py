from django.contrib.gis.db.models import fields

__author__ = 'RAJAT'
from django import forms
#from telecom_utils.models import fileModel

class UploadFileForm(forms.Form):
    """
    This class inherits the Form class
    create a form to upload the file
    """
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    #class Meta:
    #    model = fileModel
    #    fields = ('inputFileName', 'file')
