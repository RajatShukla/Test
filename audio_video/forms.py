

__author__ = 'RAJAT'
from django import  forms
from django.forms import widgets
from audio_video.models import FormModel
from parsley.decorators import parsleyfy

@parsleyfy
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

@parsleyfy
class YouTubeForm(forms.Form):
    """
    This form is used to take the URL of youtube
    and from that URL our program will tell about the
    different attributes of the video  with respect to
    given URL.
    """
    #url = forms.URLField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), label="YouTube Video URL", required=True)
    url = forms.URLField(label="YouTube Video URL", widget=widgets.TextInput(attrs={'class':'required'}))
    class Meta:
        fields = ('url')

    def clean(self):
        email = self.cleaned_data.get("url")
        if '@' not in email:
            raise forms.ValidationError("Enter valid URL")



class MyForm(forms.Form):
    title = forms.CharField(required=True, min_length=2, max_length=100, widget=widgets.TextInput(attrs={
        'class': '{required:true, minlength:2, maxlength:100}'
    }))




