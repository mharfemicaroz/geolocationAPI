from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@csrf_exempt
def generic_list(request, o, s, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                dt = o.objects.get(id=pk)
            except o.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            ds = s(dt)
            return Response(ds.data)
        else:
            dt= o.objects.all()
            ds = s(dt, many=True)
            return Response(ds.data)

    elif request.method == 'POST':
        ds = s(data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data, status=status.HTTP_201_CREATED)
        return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            dt = o.objects.get(id=pk)
        except o.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ds = s(dt, data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data)
        return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt    
def location_list(request, pk=None):
    return generic_list(request, Location, LocationSerializer, pk)