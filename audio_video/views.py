from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from audio_video.forms import UploadFileForm
from audio_video.forms import YouTubeForm
from audio_video import wave
import pafy

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
            file_ptr = wave.open("C:\Users\RAJAT\Downloads\DiscordToday\DiscordToday.wav", "rb")
            params = file_ptr.getparams()
            channel, sample_width, frame_rate = "Channel:"+str(params[0]), "Sample Width:"+str(params[1]), "Frame Rate:"+str(params[2])
            no_of_frames, comp_type, comp_name = "No of frames:"+str(params[3]), "Compression Type:"+str(params[4]), "Compression Name:"+str(params[5])
            params = channel + "\n" + sample_width + "\n" + frame_rate + "\n" + no_of_frames + "\n" + comp_type + "\n" + comp_name
            print("Parameter information", params)
            contextDict['params'] = params
            return render_to_response('audio_video/audio_info.html',contextDict,context)
    else:
        return render_to_response('audio_video/audio_info.html',contextDict,context)




def video_info(request):
    """
    This function takes the help of wave module and gives the
    detailed information about video file like frequency.
    It first upload the file to a path after that it find out
    the property of the file.
    :param request:
    :return:
    """
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': UploadFileForm, 'params':params}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Uploaded file name:", request.FILES['file'])
            file_name = request.FILES['file']
            file_ptr = wave.open("C:\Users\RAJAT\Downloads\DiscordToday\DiscordToday.wav", "rb")
            params = file_ptr.getparams()
            channel, sample_width, frame_rate = params[0], params[1], params[2]
            no_of_frames, comp_type, comp_name = params[3], params[4], params[5]
            contextDict['params'] = params
            return render_to_response('audio_video/video_info.html',contextDict,context)
    else:
        return render_to_response('audio_video/video_info.html',contextDict,context)



def youtube_video_info(request):
    """
    This function takes the youtube URL and find out
    different property of the youtube video.
    :param request:
    :return: render_to_response
    """
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': YouTubeForm, 'params':params}
    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        if form.is_valid():
            #form.save()
            url = form['url'].value()
            video = pafy.new(url)
            #Get all the attribute of the video
            params += "Title:"+str(video.title)+"\n"
            params += "Rating:"+str(video.rating)+"\n"
            params += "ViewCount:"+str(video.viewcount)+"\n"
            params += "Authoer:"+str(video.author)+"\n"
            params += "Length:"+str(video.length)+"\n"
            params += "Duration:"+str(video.duration)+"\n"
            params += "Likes:"+str(video.likes)+"\n"
            params += "Dislikes:"+str(video.dislikes)+"\n"
            params += "Description"+str(video.description)+"\n"
            #Get information about best resolution
            best = video.getbest()
            params += "Best resolution:"+str( best.resolution)+"\n"
            params + "Best extension:"+str(best.extension)+"\n"
            best.resolution, best.extension
            #Get the information about best audio
            bestaudio = video.getbestaudio()
            bestaudio.bitrate
            contextDict['params'] = params
            return render_to_response('audio_video/youtube_video_info.html',contextDict,context)
        else:
            return render_to_response('audio_video/youtube_video_info.html',contextDict,context)


    else:
        return render_to_response('audio_video/youtube_video_info.html',contextDict,context)
