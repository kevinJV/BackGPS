from django.shortcuts import render
from django.http import Http404

#----------------------Models-----------------
from .models import Profile

#----------------------Serializers------------
from .serializers import ProfileSerializer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action


class ProfileList(APIView):
    def get(self, request, format = None):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = data
            return Response(response) 
        response = serializer.errors
        return Response(response)

    def put(self, request, format = None):
        profile = self.get_object(request.data['id'])
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # permission_classes = (permissions.IsAuthenticated,)

    # @action(methods = ['get'], detail = False)
    # def all(self, request):
    #     queryset = Profile.objects.all()
    #     serializer = ProfileSerializer(queryset, many = True)
    #     return Response(serializer.data)

    # @action(methods = ['post'], detail = False)
    # def add(self, request):
    #     serializer = ProfileSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # @action(methods = ['put'], detail = False)
    # def change(self, request):
    #     profile = self.get_object(request.data['id'])
    #     serializer = ProfileSerializer(profile, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # #Este fue mapeado manualmente por si quiere updatear en la url
    # def change_url(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(profile, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)    

    # #Este fue mapeado manual para evitar que este alrevez
    # def get(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(profile)
    #     return Response(serializer.data)        
    
    # def get_object(self, pk):
    #     try:
    #         return Profile.objects.get(pk = pk)
    #     except Profile.DoesNotExist:
    #         raise Http404