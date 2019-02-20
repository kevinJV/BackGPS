from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Unidades
from .serializers import UnidadesSerializer
from rest_framework.views import APIView

#from rest_framework.permissions import TokenAuthentication

# Create your views here.
#Basicos: list, create, retrieve, update, partial_update, destroy

class UnidadesList(APIView):
    def get(self, request, format = None):
        queryset = Unidades.objects.all()
        serializer = UnidadesSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = UnidadesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = data
            return Response(response, status = status.HTTP_201_CREATED) 
        response = serializer.errors
        return Response(response, status = status.HTTP_400_BAD_REQUEST)

    # permission_classes = (permissions.IsAuthenticated,)

    # @action(methods = ['get'], detail = False)
    # def all(self, request):
    #     queryset = Unidades.objects.all()
    #     serializer = UnidadesSerializer(queryset, many = True)
    #     return Response(serializer.data)

    # @action(methods = ['post'], detail = False)
    # def add(self, request):
    #     serializer = UnidadesSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # @action(methods = ['put'], detail = False)
    # def change(self, request):
    #     unidades = self.get_object(request.data['id'])
    #     serializer = UnidadesSerializer(unidades, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # #Este fue mapeado manualmente por si quiere updatear en la url
    # def change_url(self, request, pk):
    #     unidades = self.get_object(pk)
    #     serializer = UnidadesSerializer(unidades, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)    

    # #Este fue mapeado manual para evitar que este alrevez
    # def get(self, request, pk):
    #     unidades = self.get_object(pk)
    #     serializer = UnidadesSerializer(unidades)
    #     return Response(serializer.data)        
    
    # def get_object(self, pk):
    #     try:
    #         return Unidades.objects.get(pk = pk)
    #     except Unidades.DoesNotExist:
    #         raise Http404 

# class UnidadesView(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticated,) 
#     #authentication_classes = (TokenAuthentication,)
#     queryset = Unidades.objects.all()    
#     serializer_class = UnidadesSerializer

