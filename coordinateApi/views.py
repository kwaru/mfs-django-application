from django.shortcuts import render
from rest_framework import generics
from .models import Coordinates
from .coordinateserilaizer import CoordinateSerializer

#generic view supports GET and POST http methods/verbs.
class  ListVIewpAPI(generics.ListCreateAPIView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializer

#generic view which supports Retrieval of a single resource(GET) ,update(PUT) and deletion(DELETE) .
# to get a specific resource  unique identifier(resource id) is sent together with the request e.g
# host/api/v1/coordinates/4 , here 4 is id of the resource already created before
class DetailedViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializer
