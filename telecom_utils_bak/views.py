__author__ = 'RAJAT'
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from telecom_utils.forms import UploadFileForm

def indexView(request):
    context=RequestContext(request)
    context_dict = {'forms': UploadFileForm }
    return render_to_response('telecom_utils/telecom.html', context_dict, context)

def handleOpenFile(f):
    with open("test.txt",'wb') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

def fileUpload(request):
    context = RequestContext(request)
    contextDict = {'forms': UploadFileForm}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            print("Uploaded file name:", request.FILES['file'])
            handleOpenFile( request.FILES['file'] )
            return render_to_response('telecom_utils/fileUpload.html',contextDict,context)
    else:
        return render_to_response('telecom_utils/fileUpload.html',contextDict,context)
