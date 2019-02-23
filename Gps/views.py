from django.shortcuts import render
from django.http import Http404

#----------------------Models-------------------------
from .models import Gps

#----------------------Serializers--------------------
from .serializers import GpsSerializer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action


class GpsList(APIView):
    def get(self, request, format = None):
        queryset = Gps.objects.all()
        serializer = GpsSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = GpsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = data
            return Response(response) 
        response = serializer.errors
        return Response(response)



# # Create your views here.

# class GpsView(viewsets.ViewSet):
#     permission_classes = (permissions.IsAuthenticated,)

#     @action(methods = ['get'], detail = False)
#     def all(self, request):
#         queryset = Gps.objects.all()
#         serializer = GpsSerializer(queryset, many = True)
#         return Response(serializer.data)

#     @action(methods = ['post'], detail = False)
#     def add(self, request):
#         serializer = GpsSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     @action(methods = ['put'], detail = False)
#     def change(self, request):
#         gps = self.get_object(request.data['id'])
#         serializer = GpsSerializer(gps, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     #Este fue mapeado manualmente por si quiere updatear en la url
#     def change_url(self, request, pk):
#         gps = self.get_object(pk)
#         serializer = GpsSerializer(gps, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     #Este fue mapeado manual para evitar que este alrevez
#     def get(self, request, pk):
#         gps = self.get_object(pk)
#         serializer = GpsSerializer(gps)
#         return Response(serializer.data)

#     def get_object(self, pk):
#         try:
#             return Gps.objects.get(pk = pk)
#         except Gps.DoesNotExist:
#             raise Http404