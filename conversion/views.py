from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from conversion.forms import DateTimeForms
from conversion.forms import DateTimeEpochForms
from conversion import date_time_conversion
from conversion.forms import IPForm, IpIntegerForm, HexForm
import base64
import struct
import socket



def string_to_hex(str):
    """
    This function converts string into  hex
    :param str:
    :return:
    """
    hex_str = ""
    for i in str:
        temp_str = "%0.02X"%ord(i)
        hex_str += temp_str
    return hex_str

def string_to_octet(str):
    oct_str = ""
    for i in str:
        temp_str = oct(ord(i))
        oct_str += temp_str
    return oct_str


def string_to_base64(str):
    """
    This function converts string into base 64 string.
    :param str:
    :return:
    """
    base64_str = base64.b64encode(str)
    return base64_str



def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('conversion/conversion.html',context_dict,context)


def hex_conv(request):
    context = RequestContext(request)
    contextDict = {'forms': HexForm}
    if request.method == 'POST':
        forms = HexForm(request.POST.copy())
        if forms.is_valid():
            forms.data['hex_str'] = str(string_to_hex(forms['ascii_str'].value()))
            forms.data['base64_str'] = string_to_base64(str(forms['ascii_str'].value()))
            forms.data['ascii_str'] = str(forms['ascii_str'].value())
            forms.data['octet_str'] = string_to_octet(forms['ascii_str'].value())
            contextDict['forms'] = forms

            return render_to_response('conversion/hex_conv.html',contextDict,context)
        else:
            return render_to_response('conversion/hex_conv.html',contextDict,context)
    else:
        return render_to_response('conversion/hex_conv.html',contextDict,context)


# def ip_conv(request):
#     context=RequestContext(request)
#     context_dict = {}
#     return render_to_response('conversion/conversion.html',context_dict,context)


def date_time_conv(request):
    context = RequestContext(request)
    epoch_params = ''
    date_time_params = ''
    contextDict = {'date_time_forms': DateTimeForms, 'epoch_params':epoch_params,
                   'epoch_forms':DateTimeEpochForms, 'date_time_params':date_time_params}
    if request.method == 'POST':
        date_time_form = DateTimeForms(request.POST)
        epoch_form = DateTimeEpochForms(request.POST)
        if date_time_form.is_valid():
            #Extract all the details from two forms
            year = str(date_time_form['year'].value())
            month = str(date_time_form['month'].value())
            day = str(date_time_form['day'].value())
            hour = str(date_time_form['hour'].value())
            minute = str(date_time_form['minute'].value())
            second = str(date_time_form['second'].value())
            epoch_time = str(epoch_form['input_value'].value())
            ret_list = date_time_conversion.date_time_conversion(epoch_time, year, month, day, hour, minute, second)
            date_time_params = ret_list[0]
            epoch_params = ret_list[1]
            contextDict['date_time_forms'] = date_time_form
            contextDict['epoch_form'] = epoch_form
            contextDict['epoch_params'] = epoch_params
            contextDict['date_time_params'] = date_time_params
            return render_to_response('conversion/date_time.html',contextDict,context)
        else:
            return render_to_response('conversion/date_time.html',contextDict,context)
    else:
        return render_to_response('conversion/date_time.html',contextDict,context)




def ip_conv(request):
    context = RequestContext(request)
    ip_int = ''
    ip_val = ''
    contextDict = {'ip_form': IPForm, 'ip_int':ip_int,
                   'ip_int_forms':IpIntegerForm, 'ip_val':ip_val}
    if request.method == 'POST':
        ip_form = IPForm(request.POST.copy())
        ip_int_form = IpIntegerForm(request.POST)
        if ip_form.is_valid():
            #Extract all the details from two forms
            ip_value = ip_form['ip_field'].value()
            ip_int_value = ip_int_form['ip_int_field'].value()
            print "IP values",ip_value, ip_int_value
            #ip_int = ip2int(ip_val)
            #ip_val = int2ip(int(1234567))
            ip_form.data['ip_field'] = '10.10.10.11'
            ip_form.data['ip_int_field'] = '101011'
            contextDict['ip_form'] = ip_form
            contextDict['ip_int_forms'] = ip_int_form
            contextDict['ip_int'] = ip_int
            contextDict['ip_val'] = ip_val
            return render_to_response('conversion/IP.html',contextDict,context)
        else:
            return render_to_response('conversion/IP.html',contextDict,context)
    else:
        return render_to_response('conversion/IP.html',contextDict,context)


