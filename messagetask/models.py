from django.db import models
from datetime import datetime,date
# Create your models here.
class Messages((models.Model)):
    sender=models.CharField ( max_length=200, null=True, blank=True) 
    reciever=models.CharField ( max_length=200, null=True, blank=True) 
    message=models.CharField ( max_length=200, null=True, blank=True) 
    subject=models.CharField ( max_length=200, null=True, blank=True)
    creation_date=models.DateTimeField(default=datetime.now)
    read=models.BooleanField(("read"))