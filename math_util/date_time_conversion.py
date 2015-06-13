__author__ = 'RAJAT'
import time
import datetime
import calendar

def date_time_conversion(input_value, operation_type):
    """
    This function takes input value and convert according to given format
    :param input_value:
    :param operation_type:
    :return:
    operation_types = (('1','Date Time to Epoch Time'), ('2','Epoch Time to Date Time'))
    """

    if int(operation_type) == 1:
        #Convert date time to epoch time

