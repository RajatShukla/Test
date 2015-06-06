from email import message
from django.db import models

# Create your models here.
#Create contact us class


class Base64Form(models.Model):

    inputText = models.CharField(max_length=50, unique=False)
    outputText = models.CharField(max_length=100, unique=False)
    choiceFields = models.TextField()

    def __str__(self):
        return self.name, self.emailAddress, self.subject, self.message