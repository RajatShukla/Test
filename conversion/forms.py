__author__ = 'RAJAT'
from django import forms
import time

class DateTimeEpochForms(forms.Form):
    """
    This form is used to convert epoch time to date time value.
    """
    input_value = forms.IntegerField(initial=str(int(time.time())))
    class Meta:
        fields = ('Input Value')


class DateTimeForms(forms.Form):
    """
    This form is used to convert date time to epoch time
    """
    str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
    year_int, month_int, day_int, hour_int, minute_int, second_int = str[0:4], str[5:7], str[8:10], str[11:13], str[14:16], str[17:19]
    year = forms.IntegerField(min_value=1970, initial=year_int)
    month = forms.IntegerField(max_value=12, min_value=1, initial=month_int)
    day = forms.IntegerField(max_value=31, min_value=1, initial=day_int)
    hour = forms.IntegerField(max_value=23, min_value=0, initial=hour_int)
    minute = forms.IntegerField(max_value=60, min_value=0, initial=minute_int)
    second = forms.IntegerField(max_value=59, min_value=0, initial=second_int)
    class Meta:
        fields = ('Year', 'Month', 'Day', 'Hour', 'Second')



class IPForm(forms.Form):
    """
    This form is used to create IP address data
    """
    ip_field = forms.IPAddressField()
    ip_int_field = forms.IntegerField()
    class Meta:
        fields = ('IP', 'IPIntegerField')

class IpIntegerForm(forms.Form):
    """
    This form is used to convert Integer field into IP address field
    """
    ip_int_field = forms.IntegerField()
    class Meta:
        fields = ('Integer IP')


class HexForm(forms.Form):
    """
    This is the form for the creation of hex form
    for different input formats
    """
    hex_str = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Input string")
    base64_str = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Input string")
    ascii_str = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Input string")
    octet_str = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), max_length=600, initial="Input string")


