__author__ = 'RAJAT'
from django import  forms
from telecom_utils.models import FormModel
from telecom_utils.models import SmsPduModel

class UploadFileForm(forms.ModelForm):
    """
    This class inherits the Form class
    create a form to upload the file
    """
    title = forms.CharField(max_length=100)
    file = forms.FileField()
    class Meta:
        model = FormModel
        fields = ('title', 'file')


class SmsPduForm(forms.ModelForm):
    """
    This class generates the SMS PDU form
    """
    pduType = (('1','SMS-SUBMIT'), ('2','SMS-DELIVER'))
    encoding = (('0','7 BIT'), ('8','UCS2'))
    Address = forms.CharField(max_length=20, min_length=5, required=True, label="Target Address",
                               initial="+917654321")

    SMSC = forms.CharField(max_length=13, min_length=5,required=True, label="SMSC Address",
                        initial="+91244414")

    PDUType = forms.ChoiceField(widget=forms.RadioSelect, choices=pduType, required=True,
                                label="PDU Type", initial=pduType[0])

    EncodingType = forms.ChoiceField(widget=forms.RadioSelect, choices=encoding, required=True, label="Encoding Type",
                                     initial=encoding[0])

    Text = forms.CharField(widget=forms.Textarea(attrs={'row':6, 'cols':50}),required=True, label="SMS Text",
                           initial="Hello", max_length=140)

    smsPDU = forms.CharField(widget=forms.Textarea(attrs={'row':6, 'cols':50}),required=True, label="SMS PDU",
                           initial="Hello", max_length=140)
    class  Meta:
        model = SmsPduModel
        fields = ('Address', 'SMSC', 'PDUType', 'EncodingType', 'Text', 'smsPDU')



class SmsPduEncodingForm(forms.ModelForm):
    """
    This class generates the SMS PDU form
    """
    pduType = (('1','SMS-SUBMIT'), ('2','SMS-DELIVER'))
    encoding = (('0','7 BIT'), ('8','UCS2'))
    Address = forms.CharField(max_length=20, min_length=5, required=True, label="Target Address",
                               initial="+917654321")

    SMSC = forms.CharField(max_length=13, min_length=5,required=True, label="SMSC Address",
                        initial="+91244414")

    PDUType = forms.ChoiceField(widget=forms.RadioSelect, choices=pduType, required=True,
                                label="PDU Type", initial=pduType[0])

    EncodingType = forms.ChoiceField(widget=forms.RadioSelect, choices=encoding, required=True, label="Encoding Type",
                                     initial=encoding[0])

    Text = forms.CharField(widget=forms.Textarea(attrs={'row':6, 'cols':50}),required=True, label="SMS Text",
                           initial="Hello", max_length=140)




    #Meta class of the form
    class Meta:
        model = SmsPduModel
        fields = ('Address', 'SMSC', 'PDUType', 'EncodingType', 'Text')


    def clean(self):
        self.smsPDU = "This PDU is just for testing purpose"








class PcaPGenerationForm(forms.Form):
    """
    This class generates the form for the Pcap genration
    """
    networkType = (('0','LINKTYPE_NULL'), ('1','LINKTYPE_ETHERNET'), ('3','LINKTYPE_AX25'),
                   ('7','LINKTYPE_ARCNET_BSD'))
    buffer = forms.CharField(widget=forms.Textarea, required=True, label="Input Buffer")
    choiceField = forms.ChoiceField(widget=forms.Select, choices=networkType,
                                    required=True, label="Network Type")


