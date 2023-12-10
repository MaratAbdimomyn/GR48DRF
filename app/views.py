from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import *
from .serializers import *

"""class CarsAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer"""

class CarsAPIView(APIView):
    def get(self, request):
        queryset = Cars.objects.all().values()
        return Response({'cars': list(queryset)})
    
    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'cars': serializer.data})
    
    """def put(self, request, *args, **kwargs):
        instance = Cars.objects.get(pk=pk)"""