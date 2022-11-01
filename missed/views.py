from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Dane
from .serializer import DaneSerial
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def dane_list(request):
    dane = {"slackUsername": "L0rd_5n0w", "backend": True, "age": 21, "bio": "Nerdy, will probably rule the world"}
    return Response(dane)
# def dane_list(request):
#     if request.method == 'GET':
#         dane = Dane.objects.all()
#         serializer = DaneSerial(dane, many=True)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'POST':
#         data = dict(request)
#         serializer = DaneSerial(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)