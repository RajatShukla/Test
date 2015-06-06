from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from audio_video.forms import UploadFileForm
from audio_video import wave

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('audio_video/audio_video.html',context_dict,context)



def audio_info(request):
    """
    This function takes the help of wave module and gives the
    detailed information about audio file like frequency.
    It first upload the file to a path after that it find out
    the property of the file.
    :param request:
    :return:
    """
    context = RequestContext(request)
    contextDict = {'forms': UploadFileForm}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Uploaded file name:", request.FILES['file'])
            file_name = request.FILES['file']
            file_ptr = wave.open(file_name, "rb")
            params = file_ptr.getparams()
            channel, sample_width, frame_rate = params[0], params[1], params[2]
            no_of_frames, comp_type, comp_name = params[3], params[4], params[5]
            contextDict['params'] = params
            return render_to_response('audio_video/audio_info.html',contextDict,context)
    else:
        return render_to_response('audio_video/audio_info.html',contextDict,context)
