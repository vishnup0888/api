from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# # Create your views here.
# @csrf exempt
# def fun1(request,pk):
#     try:
#         demo=student.object.get(pk=pk)
#         print('helo')
#     except:
#         return HttpResponse ("invalid")
#     if request.method=='GET':
#         S=studModelserializer(demo)
#         return JsonResponse(s.data)
#     elif request.method=='PUT':
#         d=JSONparser





# @api_view(['GET','PUT' 'DELETE'])
# def fun1(req,pk):
#     try:
#         demo=student.objects.get(pk=pk)
#     except student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)    
#     if req.method=='GET':
#         s=studmodelizer(demo)
#         return Response(s.data)
#     elif req.method =='PUT':
#         s=studmodelizer(demo,data=req.data)
#         if s. is_valid():
#             s.save
#             d = student.objects.all()
#         s = studmodelizer(data=req.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.save)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif req.method=='DELETE':
#         demo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT','DELETE'])
def fun1(req,pk):
    try:
        demo=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=studmodelizer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=studmodelizer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
             
