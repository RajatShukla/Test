__author__ = 'RAJAT'
# from django.db import models
# from time import time
# """
# This class simulates the model of the file uploading form
# """
#
# def getUploadFileName(instance, fileName):
#     return 'uploaded_files/%s_%s' %(str(time()).replace('.','_'),fileName)
#
# class fileModel(models.Model):
#     """
#     This class creates the model of the
#     file uploading form
#     """
#     inputFileName = models.CharField(max_length=50)
#     file = models.FileField(upload_to=getUploadFileName)
