from django.shortcuts import render
from django.http import HttpResponse
from .models import Messages
import json
from django.db.models import Case, CharField, Value, When
from django.core import serializers
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello World")
@csrf_exempt
def write_message(request):
    if request.method == 'POST':
        message = Messages()
        message.sender= request.POST.get('sender')
        message.reciever= request.POST.get('reciever')
        message.message= request.POST.get('message')
        message.subject= request.POST.get('subject')
        message.creation_date= datetime.now()
        message.read=False
        message.save()
        return HttpResponse("message was created successfully")
def get_all_messages(request,user):
    messages=Messages.objects.filter(reciever=user)
    qs_json = serializers.serialize('json', messages)
    for x in messages:
        x.creation_date=x.creation_date
        x.read=True
        x.save()
    return HttpResponse(qs_json, content_type='application/json')
def get_all_unread_messages(request,user):
    messages=Messages.objects.filter(reciever=user,read=False)
    qs_json = serializers.serialize('json', messages)
    for x in messages:
        x.creation_date=x.creation_date
        x.read=True
        x.save()
    return HttpResponse(qs_json, content_type='application/json')
def delete_message(request,mpk,user):
    try:
        y=Messages.objects.get(pk=mpk , sender=user)
        y.delete()
        return HttpResponse("Deleted successfully")
    except:
        pass
    try:
        x=Messages.objects.get(pk=mpk , reciever=user)
        x.delete()
        return HttpResponse("Deleted successfully")
    except:
        return HttpResponse("Cannot Delete!!!")
    