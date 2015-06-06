__author__ = 'RAJAT'
from  django import forms


class HashForm(forms.Form):

    """
    This class creates the form for hash utility

    """
    hashTypes = (('1','MD2'), ('2','MD4'), ('3','MD5'),
                  ('4','SHA-1'), ('5','SHA-224'),('6','SHA-256'),
                 ('7','SHA-384'),('8','SHA-512'),('9','RIPEMD'))
    inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Hello")
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=hashTypes, initial='1', required=True)

    class Meta:
        #model = HashForm
        fields = ('Input Text',  'Choice Fields')




class EncryptionForm(forms.Form):

    """
    This class creates the form for Encryption utility

    """
    encryptionTypes = (('1','AES'), ('2','ARC2'), ('3','ARC4'),
                  ('4','Blowfish'), ('5','CAST'),('6','DES'),
                 ('7','DES3'),('8','PCKS1_OAEP'),('9','XOR'))
    operationType = (('1','Encrypt'), ('2','Decrypt'))
    inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Hello", required=True)
    inputKey = forms.CharField(max_length=100, initial="abc", required=True)
    choiceFields = forms.ChoiceField(widget=forms.RadioSelect, choices=encryptionTypes, initial='1', required=True)
    operation = forms.ChoiceField(widget=forms.RadioSelect, choices=operationType, initial='1', required=True)

    class Meta:
        #model = EncryptionForm
        fields = ('Input Text', 'Input Key', 'Choice Fields', 'Operation')


#Commented below code, will use it for further reference
# class HashingForm(forms.Form):
#     inputText = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Input string")
#     class Meta:
#         fields = ('Input Text')
#
# class EncryptionForm(forms.Form):
#     inputText = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':50}), max_length=600, initial="Input String")
#     key = forms.CharField(max_length=300,min_length=30, initial="Key")
#     class Meta:
#         fields =('Input Text', 'Key')
#
# class RSAForm(forms.Form):
#     inputText = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':50}), max_length=600, initial="Input String")
#     publicKey = forms.CharField(max_length=100, min_length=1, initial="Public Key")
#     privateKey = forms.CharField(max_length=100, min_length=1, initial="Public Key")
#     class Meta:
#         fields = ('Input Text', 'Public Key', 'Private Key')

