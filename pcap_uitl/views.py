from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('pcap_util/pcap_util.html',context_dict,context)