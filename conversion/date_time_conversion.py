__author__ = 'RAJAT'
import time
import datetime
import calendar

def date_time_conversion(epoch_time, year, month, day, hour, minute, second):
    """
    This function takes input value and convert according to given format
    :param input_value:
    :param operation_type:
    :return:
    operation_types = (('1','Date Time to Epoch Time'), ('2','Epoch Time to Date Time'))
    """
    if epoch_time != 'None':
        date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_time)))
    else:
        date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
    #datetime.datetime(2012,04,01,0,0).strftime('%s')
    if year != 'None':
        #epoch_time = datetime.datetime(year=int(year), month=int(month), day=int(day),
        #              hour=int(hour), minute=int(minute), second=int(second)).strftime('%s')
        epoch_time = str(time.mktime((int(year), int(month), int(day),
                      int(hour), int(minute), int(second),
                     12345, 1 ,1)))
    else:
        epoch_time = str(int(time.time()))
    return [date_time, epoch_time]
    time.mktime()


