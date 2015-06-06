__author__ = 'RAJAT'
from django import  forms
from audio_video.models import FormModel


class UploadFileForm(forms.ModelForm):
    """
    This class inherits the Form class
    create a form to upload the file
    """


    title = forms.CharField(max_length=100)
    file = forms.FileField()
    class Meta:
        model = FormModel
        fields = ('title','file')


