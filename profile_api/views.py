from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return all the feature of APIView"""
        an_apiview=[
            'Uses HTTP methods as funtion (GET,POST,PATCH,PUT, DELETE)',
            'Is similer to a traditional Django view',
            'Give most control over application logic',
            'is Mapped mannually to URLs',
        ]
        
        return Response({'message' : 'Hello!' , 'an_apiview': an_apiview})
