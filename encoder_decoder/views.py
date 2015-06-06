__author__ = 'RAJAT'
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from encoder_decoder.forms import Base64DecoderForm
from encoder_decoder.forms import Base64EncoderForm
import base64
from encoder_decoder import encode_decode

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('encoder_decoder/encoder_decoder.html',context_dict,context)


def base64Encoder(request):
    context = RequestContext(request)
    if request.method == 'POST':
        encoded_form = Base64EncoderForm(request.POST)
        if encoded_form['inputText'].value() != '' and encoded_form['choiceFields'].value() != '':
            encoded_str = encode_decode.encoder(encoded_form['inputText'].value(), int(encoded_form['choiceFields'].value()))

        else:
            encoded_str = ""
        context_dict = {'form': encoded_form, 'encoded_str':encoded_str }

    else:
         encoded_str = ""
         context_dict = {'form': Base64EncoderForm, 'encoded_str':encoded_str }
    return render_to_response('encoder_decoder/base64Encoder.html',context_dict,context)



def base64Decoder(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form_for_decoding = Base64DecoderForm(request.POST)
        if ( form_for_decoding['inputText'].value() != '' and form_for_decoding['choiceFields'].value() != ''):
            decoded_str = encode_decode.decoder(form_for_decoding['inputText'].value(), int(form_for_decoding['choiceFields'].value()))
        else:
            decoded_str = ""
        context_dict = {'form':form_for_decoding, 'decoded_str':decoded_str}
    else:
        decoded_str = ""
        context_dict = {'form':Base64DecoderForm, 'decoded_str':decoded_str}
    
    return render_to_response('encoder_decoder/base64Decoder.html',context_dict,context)