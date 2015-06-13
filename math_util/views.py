from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from math_util.forms import NumberForms
from math_util.forms import PowLogForms
from math_util.forms import TrigonmetryForms
from math_util.forms import HyperbolicForms
from math_util.forms import MatrixForm

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/math_util.html',context_dict,context)


def number_theoretic(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': NumberForms, 'params':params}
    if request.method == 'POST':
        form = NumberForms(request.POST)
        if form.is_valid():
            #form.save()
            input_val  = form['input_value'].value()
            oprn_val  = form['choiceFields'].value()
            return render_to_response('math_util/number_theoretic.html',contextDict,context)
        else:
            return render_to_response('math_util/number_theoretic.html',contextDict,context)


    else:
        return render_to_response('math_util/number_theoretic.html',contextDict,context)

def pow_log(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': PowLogForms, 'params':params}
    if request.method == 'POST':
        form = PowLogForms(request.POST)
        if form.is_valid():
            #form.save()
            input_val1  = form['inp_val1'].value()
            input_val2  = form['inp_val2'].value()
            oprn_val  = form['choiceFields'].value()
            return render_to_response('math_util/pow_log.html',contextDict,context)
        else:
            return render_to_response('math_util/pow_log.html',contextDict,context)
    else:
        return render_to_response('math_util/pow_log.html',contextDict,context)



def trigon_fun(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': TrigonmetryForms, 'params':params}
    if request.method == 'POST':
        form = TrigonmetryForms(request.POST)
        if form.is_valid():
            #form.save()
            input_val1  = form['inp_val1'].value()
            #input_val2  = form['inp_val2'].value()
            oprn_val  = form['choiceFields'].value()
            return render_to_response('math_util/trigon_fun.html',contextDict,context)
        else:
            return render_to_response('math_util/trigon_fun.html',contextDict,context)
    else:
        return render_to_response('math_util/trigon_fun.html',contextDict,context)



def hyperbolic_fun(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': HyperbolicForms, 'params':params}
    if request.method == 'POST':
        form = HyperbolicForms(request.POST)
        if form.is_valid():
            #form.save()
            input_val1  = form['inp_val1'].value()
            #input_val2  = form['inp_val2'].value()
            oprn_val  = form['choiceFields'].value()
            return render_to_response('math_util/hyperbolic_fun.html',contextDict,context)
        else:
            return render_to_response('math_util/hyperbolic_fun.html',contextDict,context)
    else:
        return render_to_response('math_util/hyperbolic_fun.html',contextDict,context)





def matrix_fun(request):
    #context=RequestContext(request)
    #context_dict = {'forms':MatrixForm}
    #return render_to_response('math_util/matrix_fun.html',context_dict,context)
    #def my_matrix(request):
    [nrows,ncols] = [3,4]

    my_form = MatrixForm(nrows=nrows, ncols=ncols)
    return render_to_response('math_util/matrix_fun.html', RequestContext(request,
                        {'forms':my_form, "nrows":range(nrows), "ncols":range(ncols), 'rows':range(0,2,1), 'cols':range(0,2,1)}))


