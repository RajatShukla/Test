from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('hex_editor/hex_editor.html',context_dict,context)