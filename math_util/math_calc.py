from sympy.mpmath.math2 import math_log
import math

__author__ = 'RAJAT'
#This module is responsible for maths related calculations

def num_theoritic_calc(inp_no, opn_type):
    oprn_dic = {'1': 'celing_func', '2':'Factorial', '3':'Floor', '4':'Regular expression'}
    if int(opn_type) == 1:
        #Do calculation for celing function
        ceil_val = math.ceil(float(inp_no))
        return ceil_val
    if int(opn_type) == 2:
        #Do calculation for factorial function
        factorial = math.factorial(int(inp_no))
        return factorial
    if int(opn_type) == 3:
        #Do calculation for floor function
        floor_val = math.floor(float(inp_no))
        return floor_val
    if int(opn_type) == 4:
        #Do calculation for regular expression
        #it return exponential and mantissa
        mantissa, exp = math.frexp(float(inp_no))
        return str(mantissa)+ "," + str(exp)
    else:
        return "Invalid operation type"

def pow_log_calc(inp_val1, inp_val2, opn_type):
    oprn_dic = {'1': 'Power_func', '2':'Log_func'}
    if int(opn_type) == 1:
        output = math.pow(float(inp_val1), float(inp_val2))
        return str(output)
    if int(opn_type) == 2:
        output = math.log(int(inp_val1), int(inp_val2))
        return str(output)


def trigon_calc(inp_val1, opn_type):
    oprn_dic = {
        '1': 'arc cosine of x, in radians', '2':'arc sine of x, in radians',
        '3':'arc tangent of x, in radians', '4':'cosine of x radians',
        '5':'sine of x radians', '6':'tangent of x radians'}

    if int(opn_type) == 1:
        output = math.acos(float(inp_val1))
        return str(output)
    if int(opn_type) == 2:
        output = math.asin(float(inp_val1))
        return str(output)
    if int(opn_type) == 3:
        output = math.atan(float(inp_val1))
        return str(output)
    if int(opn_type) == 4:
        output = math.cos(float(inp_val1))
        return str(output)
    if int(opn_type) == 5:
        output = math.sin(float(inp_val1))
        return str(output)
    if int(opn_type) == 6:
        output = math.tan(float(inp_val1))
        return str(output)
    else:
        return "Invalid Operation"

def hyperbolic_fun_cal(inp_val1, opn_type):
     oprn_dic = {
        '1': 'inverse hyperbolic cosine of x', '2':'inverse hyperbolic sine of x',
        '3':' inverse hyperbolic tangent of x', '4':'hyperbolic cosine of x',
        '5':'hyperbolic sine of x', '6':'hyperbolic tangent of x'}
     if int(opn_type) == 1:
         output = math.acosh(float(inp_val1))
         return str(output)
     if int(opn_type) == 2:
         output = math.asinh(float(inp_val1))
         return str(output)
     if int(opn_type) == 3:
         output = math.atanh(float(inp_val1))
         return str(output)
     if int(opn_type) == 4:
         output = math.cosh(float(inp_val1))
         return str(output)
     if int(opn_type) == 5:
         output = math.sinh(float(inp_val1))
         return str(output)
     if int(opn_type) == 6:
         output = math.tanh(float(inp_val1))
         return str(output)
     else:
         return "Invalid Operation"







