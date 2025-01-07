from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf exempt
def fun1(request,pk):
    try:
        demo=student.object.get(pk=pk)
        print('helo')
    except:
        return HttpResponse ("invalid")
    if request.method=='GET':
        S=studModelserializer(demo)
        return JsonResponse(s.data)
    elif request.method=='PUT':
        d=JSONparser
