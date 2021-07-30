from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Coordinates
from .coordinateserilaizer import CoordinateSerializer
from  .utility import nearestpairpoints

#View functionas which handle points in string format resource creation and fetching

@csrf_exempt
def coordinate_list(request):
#get method , getting all rescources created before
    if request.method == 'GET':
        coordinates = Coordinates.objects.all()
        serializer = CoordinateSerializer(coordinates,many= True)
        return JsonResponse(serializer.data,safe= False)

#post method , creating a new resource
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = CoordinateSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors,status = 400)


