from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import *
from .serializers import studentserializer
class studentRecord(APIView):
    def get(self,request):
        Student=student.objects.all()
        serializer=studentserializer(Student,many=True)
        return Response(serializer.data)
    def post(self):
        pass

