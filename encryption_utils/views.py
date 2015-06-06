__author__ = 'RAJAT'
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from forms import HashForm
from forms import EncryptionForm
import hasing
import encryption_decryption



#Method to handle the hashed string of a string
def hashing(request):
    context = RequestContext(request)
    if request.method == 'POST':
        hash_form = HashForm(request.POST)
        if hash_form['inputText'].value() != '' and hash_form['choiceFields'].value() != '':
            hashed_str = hasing.hash(str(hash_form['inputText'].value()), int(hash_form['choiceFields'].value()))

        else:
            hashed_str = ""
        context_dict = {'form': hash_form, 'hashed_str':hashed_str}

    else:
         hashed_str = ""
         context_dict = {'form': HashForm, 'hashed_str':hashed_str }
    return render_to_response('encryption_utils/hashing.html',context_dict, context)


#Method for handling encryption and decryption
def encrypt_decrypt(request):
    context = RequestContext(request)
    if request.method == 'POST':
        encr_form = EncryptionForm(request.POST)
        if (encr_form['inputText'].value() != '' and encr_form['choiceFields'].value() != '') and encr_form['inputKey'].value() != '':
            encr_str =  encryption_decryption.encrypt_decrypt(input_text=str(encr_form['inputText'].value()),
                                                              input_key=str(encr_form['inputKey'].value()),
                                                              encryption_type=int(encr_form['choiceFields'].value()),
                                                              operatation=int(encr_form['operation'].value())
                                                              )

        else:
            encr_str = ""
        context_dict = {'form':encr_form, 'encr_str':encr_str}

    else:
         encr_str = ""
         context_dict = {'form':EncryptionForm, 'encr_str':encr_str }
    return render_to_response('encryption_utils/encrypt_util.html',context_dict,context)


#Method for handling the RSA algorithm
def rsa_algo(request):
    pass


def index_view(request):
    context = RequestContext(request)
    dict = {}
    return render_to_response('encryption_utils/encrypt_util.html', dict, context)
