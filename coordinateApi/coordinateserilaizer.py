from rest_framework import serializers
from .models import Coordinates
from django.contrib.auth.models import User

#Serializing  Coordinate instance


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'
        


