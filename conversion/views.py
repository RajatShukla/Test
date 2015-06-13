from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from registration.views import _RequestPassingFormView
from conversion.forms import DateTimeForms

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('conversion/conversion.html',context_dict,context)


def hex_conv(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('conversion/conversion.html',context_dict,context)


def ip_conv(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('conversion/conversion.html',context_dict,context)


def date_time_conv(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': DateTimeForms, 'params':params}
    if request.method == 'POST':
        form = DateTimeForms(request.POST)
        if form.is_valid():
            #form.save()
            #input_val1  = form['inp_val1'].value()
            #input_val2  = form['inp_val2'].value()
            #oprn_val  = form['choiceFields'].value()
            params = math_calc.hyperbolic_fun_cal(input_val1, oprn_val)
            contextDict['params'] = params
            return render_to_response('conversion/date_time.html',contextDict,context)
        else:
            return render_to_response('conversion/date_time.html',contextDict,context)
    else:
        return render_to_response('conversion/date_time.html',contextDict,context)