from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from sup.models import Supplier
from sup.serializers import SupplierSerializer
from rest_framework import generics

# Create your views here.
class SupplierList(generics.ListCreateAPIView):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
 
    serializer_class = SupplierSerializer