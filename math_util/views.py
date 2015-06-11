from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/math_util.html',context_dict,context)


def number_theoretic(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/number_theoretic.html',context_dict,context)


def pow_log(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/pow_log.html',context_dict,context)


def trigon_fun(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/trigon_fun.html',context_dict,context)



def hyperbolic_fun(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/hyperbolic_fun.html',context_dict,context)



def matrix_fun(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/math_util.html',context_dict,context)


