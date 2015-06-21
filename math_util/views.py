from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from math_util.forms import NumberForms
from math_util.forms import PowLogForms
from math_util.forms import TrigonmetryForms
from math_util.forms import HyperbolicForms
from math_util.forms import MatrixForm
import math_util.math_calc as math_calc

def indexView(request):
    context=RequestContext(request)
    context_dict = {}
    return render_to_response('math_util/math_util.html',context_dict,context)


def number_theoretic(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': NumberForms, 'params':params}
    if request.method == 'POST':
        form = NumberForms(request.POST.copy())
        if form.is_valid():
            error_list = []
            #form.save()
            input_val  = form['input_value'].value()
            oprn_val  = form['choiceFields'].value()
            form.data['input_value'] = input_val
            form.data['choiceFields'] = oprn_val

            if input_val == '':
                error_list.append("Integer field is required")
            if oprn_val == '':
                error_list.append("Please select operation")
            try:
                input_val = float(input_val)
                params = math_calc.num_theoritic_calc(input_val, oprn_val)
            except ValueError:
                error_list.append("Require a number")


            contextDict['params'] = params
            contextDict['errors'] = error_list
            contextDict['forms'] = form
            return render_to_response('math_util/number_theoretic.html',contextDict,context)
        else:
            error_list = []
            error_list.append("Integer field is required")
            error_list.append("Please select operation")
            contextDict['errors'] = error_list
            return render_to_response('math_util/number_theoretic.html',contextDict,context)


    else:
        return render_to_response('math_util/number_theoretic.html',contextDict,context)

def pow_log(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': PowLogForms, 'params':params}
    if request.method == 'POST':
        form = PowLogForms(request.POST.copy())
        if form.is_valid():
            #form.save()
            error_list = []
            input_val1  = form['inp_val1'].value()
            input_val2  = form['inp_val2'].value()
            oprn_val  = form['choiceFields'].value()
            form.data['inp_val1'] = input_val1
            form.data['inp_val2'] = input_val2
            form.data['choiceFields'] = oprn_val
            if input_val1 == '':
                error_list.append("Integer field is required for input value1")
            if input_val2 == '':
                error_list.append("Integer field is required for input value2")
            if oprn_val == '':
                error_list.append("Please select operation")
            try:
                input_val1 = float(input_val1)
                input_val2 = float(input_val2)
                params = math_calc.pow_log_calc(input_val1, input_val2, oprn_val)
            except ValueError:
                error_list.append("Require a number")
            

            contextDict['params'] = params
            contextDict['forms'] = form
            contextDict['errors'] = error_list
            return render_to_response('math_util/pow_log.html',contextDict,context)
        else:
            error_list = []
            if form['inp_val1'].value() == '':
                error_list.append("Integer field is required for input value1")
            if form['inp_val2'].value() == '':
                error_list.append("Integer field is required for input value2")
            if form['choiceFields'].value() == '':
                error_list.append("Please select operation")
            contextDict['errors'] = error_list
            return render_to_response('math_util/pow_log.html',contextDict,context)
    else:
        return render_to_response('math_util/pow_log.html',contextDict,context)



def trigon_fun(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': TrigonmetryForms, 'params':params}
    if request.method == 'POST':
        form = TrigonmetryForms(request.POST.copy())
        if form.is_valid():
            error_list = []
            #form.save()
            input_val1  = form['inp_val1'].value()
            form.data['inp_val1'] = input_val1
            #input_val2  = form['inp_val2'].value()
            oprn_val  = form['choiceFields'].value()
            form.data['choiceFields'] = oprn_val
            if input_val1 == '':
                error_list.append("Require a float value")
            if oprn_val == '':
                error_list.append("Please select a operation")
            try:
                params = math_calc.trigon_calc(input_val1, oprn_val)
            except ValueError:
                error_list.append("Kindly enter float value in their required format")

            contextDict['params'] = params
            contextDict['errors'] = error_list
            contextDict['forms'] = form
            return render_to_response('math_util/trigon_fun.html',contextDict,context)
        else:
            error_list = []
            if form['inp_val1'].value() == '':
                error_list.append("Integer field is required for input value1")
            if form['choiceFields'].value() == '':
                error_list.append("Please select operation")
            contextDict['errors'] = error_list
            return render_to_response('math_util/trigon_fun.html',contextDict,context)
    else:
        return render_to_response('math_util/trigon_fun.html',contextDict,context)



def hyperbolic_fun(request):
    context = RequestContext(request)
    params = ''
    contextDict = {'forms': HyperbolicForms, 'params':params}
    if request.method == 'POST':
        form = HyperbolicForms(request.POST.copy())
        if form.is_valid():
            error_list = []
            #form.save()
            input_val1  = form['inp_val1'].value()
            #input_val2  = form['inp_val2'].value()
            oprn_val  = form['choiceFields'].value()
            form.data['inp_val1'] = input_val1
            form.data['choiceFields'] = oprn_val
            if input_val1 == '':
                error_list.append("Please enter the value")
            if oprn_val == '':
                error_list.append("Please select a operation")
            try:
                params = math_calc.hyperbolic_fun_cal(input_val1, oprn_val)
            except ValueError:
                error_list.append("Kindly enter integer or float value")

            contextDict['params'] = params
            contextDict['errors'] = error_list
            contextDict['forms'] = form
            return render_to_response('math_util/hyperbolic_fun.html',contextDict,context)
        else:
            error_list = []
            if form['inp_val1'].value() == '':
                error_list.append("Please enter the value")
            if form['choiceFields'].value() == '':
                error_list.append("Please select a operation")
            contextDict['errors'] = error_list
            contextDict['forms'] = form
            return render_to_response('math_util/hyperbolic_fun.html',contextDict,context)
    else:
        return render_to_response('math_util/hyperbolic_fun.html',contextDict,context)





def matrix_fun(request):
    #context=RequestContext(request)
    #context_dict = {'forms':MatrixForm}
    #return render_to_response('math_util/matrix_fun.html',context_dict,context)
    #def my_matrix(request):
    [nrows,ncols] = [3,4]
    method = 'GET'
    if  request.method == 'POST':
        method = 'POST'
    return render_to_response('math_util/matrix_fun.html', RequestContext(request,
                        {'forms':my_form, "nrows":range(nrows), "ncols":range(ncols), 'rows':range(0,2,1), 'cols':range(0,2,1)}))


