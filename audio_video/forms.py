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

class YouTubeForm(forms.Form):
    """
    This form is used to take the URL of youtube
    and from that URL our program will tell about the
    different attributes of the video  with respect to
    given URL.
    """
    url = forms.CharField(max_length=1000)
    class Meta:
        fields = ('url')






