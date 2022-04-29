from dataclasses import fields
from rest_framework import serializers
from .models import *
class courseserializer(serializers.ModelSerializer):
    class Meta:
        model=course
        fields='__all__'

class studentserializer(serializers.ModelSerializer):
    
    class Meta:
        model=student
        fields='__all__'
    enrolled_courses=courseserializer(many=True)
