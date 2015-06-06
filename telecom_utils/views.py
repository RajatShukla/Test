__author__ = 'RAJAT'
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from telecom_utils.forms import UploadFileForm
from telecom_utils.forms import SmsPduForm
from filetransfers.api import serve_file
from telecom_utils.models import FormModel
from  telecom_utils.forms import PcaPGenerationForm
from  telecom_utils.forms import PcaPGenerationForm
import os
import tempfile
import zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render
from telecom_utils.sms_handler import SmsEncoder


def search_form(request):
    return render(request, 'telecom_utils/search_form.html')

def search(request):
    if 'q' in request.GET:
        response = 'you  search for %r ' % request.GET['q']
    else:
        response = 'you submitted empty form'
    return HttpResponse(response)


def smsHandler(request):
    context = RequestContext(request)
    if request.method == 'POST':
        method=""
        #Do for post method else do for get method
        smsPduForm = SmsPduForm(request.POST)
        smsc = smsPduForm['SMSC'].value()
        address = smsPduForm['Address'].value()
        encodingType = smsPduForm['EncodingType'].value()
        pduType = smsPduForm['PDUType'].value()
        text = smsPduForm['Text'].value()
        smsPdu = smsPduForm['smsPDU'].value()
        print(smsc,address,encodingType,pduType,text,smsPdu)
        if "Encode" in request.POST:
            method = "encode"
            smsEncObj = SmsEncoder(encodingType, smsc, pduType, text, address )
            smsPdu = smsEncObj.generateSmsSubmitPdu()
            #SmsPduForm.clean_smsPDU()
            #smsPduForm.fields["smsPDU"].initial = "This is updated PDU"
        elif "Decode" in request.POST:
            method = "decode"
        print("Action need to perform:",method)

        sms_form = SmsPduForm(None)
        sms_form['SMSC'] = smsc
        # address = smsPduForm['Address'].value()
        # encodingType = smsPduForm['EncodingType'].value()
        # pduType = smsPduForm['PDUType'].value()
        # text = smsPduForm['Text'].value()
        # smsPdu = smsPduForm['smsPDU'].value()
        # sms_form.Address = SmsPduForm.Address.
        # sms_form.encoding = SmsPduForm.encoding
        # sms_form.EncodingType = smsPduForm.EncodingType
        # sms_form.pduType = smsPduForm.pduType
        # sms_form.SMSC = smsPduForm.SMSC
        # sms_form.Text = "Hello"
        # sms_form.smsPDU = "Modified PDU"

        contextDic = {'forms':sms_form}
        return render_to_response('telecom_utils/smsUtil.html',contextDic,context)
    else:
        contextDic = {'forms':SmsPduForm}
        return render_to_response('telecom_utils/smsUtil.html',contextDic,context)

def pcapGenHandler(request):
    context = RequestContext(request)
    contextDic = {'forms':PcaPGenerationForm}
    return  render_to_response('telecom_utils/pcapGen.html',contextDic,context)


def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('telecom_utils/telecom.html',context_dict,context)



def fileUpload(request):
    context = RequestContext(request)
    contextDict = {'forms': UploadFileForm}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Uploaded file name:", request.FILES['file'])
            return render_to_response('telecom_utils/fileUpload.html',contextDict,context)
    else:
        return render_to_response('telecom_utils/fileUpload.html',contextDict,context)



# #This function handles the file download method from the site
# def fileDownloadForPcap(request):
#     context = RequestContext(request)
#     uplodedFiles = os.listdir('C:\Project\Python\DevUtils\uploaded_files')
#
#     files = []
#     for file in uplodedFiles:
#         files.append(file)
#     contextDic = {'files':files }
#     return render_to_response('telecom_utils/fileDownLoad.html', contextDic, context)




def testFile(request):
    context = RequestContext(request)
    objects = FormModel.objects.all()
    files = []
    for file in objects:
        files.extend({'title':file.title, 'file':file.file})
    return render_to_response('telecom_utils/fileDownLoad.html',{'files': objects}, context)


def testDownload(request,fileName):
    print(fileName)
    context = RequestContext(request)
    objects = FormModel.objects.all()
    files = []
    for file in objects:
        files.extend({'title':file.title, 'file':file.file})
    fileName = "uploaded_files\\" + str(fileName)
    file = open(fileName, "rb")
    wrapper = FileWrapper(file)
    #response = HttpResponse(wrapper, content_type='text/plain')
    response = HttpResponse(file.read(

    ), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s'%fileName
    return response
    #return render_to_response('telecom_utils/fileDownLoad.html',{'files': objects}, context)

def fileDownload(request):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    context = RequestContext(request)
    print(context.dicts())
    filename = "F:\Downloads\\apache-maven-3.1.1-bin.zip" # Select your file here.
    file = open(filename, "rb")
    wrapper = FileWrapper(file)
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response


def send_zipfile(request):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,
    without loading the whole file into memory. A similar approach can
    be used for large dynamic PDF files.
    """
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for index in range(10):
        filename = "F:\\Downloads\\apache-maven-3.1.1-bin.zip" # Select your files here.
        archive.write(filename, 'file%d.txt' % index)
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=test.zip'
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response
