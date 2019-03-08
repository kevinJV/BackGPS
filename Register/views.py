from django.shortcuts import render
from django.http import Http404, HttpResponse

#----------------------Models------------
from .models import Dispositivo

#----------------------Serializers------------
from .serializers import DispositivoSerializer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action


# Create your views here.

class DispositivoList(APIView):
    def get(self, request, format = None):
        queryset = Dispositivo.objects.all()
        serializer = DispositivoSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = DispositivoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = data
            return Response(response) 
        response = serializer.errors
        return Response(response)

    def put(self, request, format = None):
        dispositivo = self.get_object(request.data['id'])
        serializer = DispositivoSerializer(dispositivo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data['id']
        dispositivo = self.get_object(id)
        dispositivo.delete()
        msg = "Dispositivo " , id , " borrado con exito"
        return Response(msg)

    def get_object(self, pk):
        try:
            return Dispositivo.objects.get(pk = pk)
        except Dispositivo.DoesNotExist:
            raise Http404
        
    # permission_classes = (permissions.IsAuthenticated,)

    # @action(methods = ['get'], detail = False)
    # def all(self, request):
    #     queryset = Dispositivo.objects.all()
    #     serializer = DispositivoSerializer(queryset, many = True)
    #     return Response(serializer.data)

    # @action(methods = ['post'], detail = False)
    # def add(self, request):
    #     serializer = DispositivoSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # @action(methods = ['put'], detail = False)
    # def change(self, request):
    #     dispositivo = self.get_object(request.data['id'])
    #     serializer = DispositivoSerializer(dispositivo, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # @action(methods = ['delete'], detail = False)
    # def remove(self, request):
    #     id = request.data['id']
    #     dispositivo = self.get_object(id)
    #     dispositivo.delete()
    #     msg = "Dispositivo " , id , " borrado con exito"
    #     return HttpResponse(status = 204, content = msg)

    # #Este fue mapeado manualmente por si quiere updatear en la url
    # def change_url(self, request, pk):
    #     dispositivo = self.get_object(pk)
    #     serializer = DispositivoSerializer(dispositivo, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)    

    # #Este fue mapeado manual para evitar que este alrevez
    # def get(self, request, pk):
    #     dispositivo = self.get_object(pk)
    #     serializer = DispositivoSerializer(dispositivo)
    #     return Response(serializer.data)        
    
    # def get_object(self, pk):
    #     try:
    #         return Dispositivo.objects.get(pk = pk)
    #     except Dispositivo.DoesNotExist:
    #         raise Http404            