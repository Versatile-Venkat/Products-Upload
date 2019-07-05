from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from reg.models import Registration
from reg.serializers import RegistrationSerializer
from rest_framework import generics
class RegistrationList(generics.ListCreateAPIView):
    queryset=Registration.objects.all()
    serializer_class=RegistrationSerializer
class RegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
 
    serializer_class = RegistrationSerializer


 
