from rest_framework import serializers
from .models import *

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['brand', 'model', 'engine', 'power']