from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Coordinates
from .coordinateserilaizer import CoordinateSerializer
from  .utility import nearestpairpoints
@csrf_exempt
def coordinate_list(request):

    if request.method == 'GET':
        coordinates = Coordinates.objects.all()
        serializer = CoordinateSerializer(coordinates,many= True)
        return JsonResponse(serializer.data,safe= False)


    elif request.method=='POST':
      
        data = JSONParser().parse(request)
        print(data)
       
        mylist1 = list(eval(data['submitted_coordinate']))
    
        print(list(nearestpairpoints(mylist1)))
        print(str(list(nearestpairpoints(mylist1))))
        #data['closet_paircoordinates'] = str(list(nearestpairpoints(mylist1)))
        print(data)
        serializer = CoordinateSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors,status = 400)


