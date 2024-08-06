from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializer

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializer.HelloSerializers
    
    def get(self, request, format=None):
        """Return all the feature of APIView"""
        an_apiview=[
            'Uses HTTP methods as funtion (GET,POST,PATCH,PUT, DELETE)',
            'Is similer to a traditional Django view',
            'Give most control over application logic',
            'is Mapped mannually to URLs',
        ]
        
        return Response({'message' : 'Hello!' , 'an_apiview': an_apiview})
    
    def post(self, request,format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data= request.data)
        
        if serializer.is_valid():
            name: str=serializer.validated_data.get('name')
            message: str= f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handles partially update an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
