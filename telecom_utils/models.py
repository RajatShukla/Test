__author__ = 'RAJAT'
from django.db import models
import time

def getUploadFileName(instance, fileName):
     return 'uploaded_files/%s_%s' %(str(time.time()).replace('.','_'),fileName)

class FormModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=getUploadFileName)



class SmsPduModel(models.Model):
    
    Address = models.CharField(max_length=100)
    SMSC = models.CharField(max_length=100)

    PDUType = models.CharField(max_length=100)

    EncodingType = models.CharField(max_length=100)

    Text = models.CharField(max_length=100)

    smsPDU = models.CharField(max_length=100)

    def clean(self):
        pass





