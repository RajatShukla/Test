__author__ = 'RAJAT'
from django.db import models
import time

def getUploadFileName(instance, fileName):
     return 'uploaded_files/%s_%s' %(str(time.time()).replace('.','_'),fileName)

class FormModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=getUploadFileName)








