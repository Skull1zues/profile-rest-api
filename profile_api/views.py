from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


from profile_api import serializer
from profile_api import models
from profile_api import permission



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
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class=serializer.HelloSerializers
    
    def list(self,request):
        """Returns a hello message"""
        
        a_viewset = [
            'Uses actions (list,create, retrieve, update, partial_update,destroy)',
            'Automatically maps to urls using routers',
            'Provide more functionality with less code',
            
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk=None):
        """Handles getting an object by id"""
        return Response({'http_method':'METHOD:GET'})
    
    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handle partial updating an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handle deleteing an object"""
        return Response({'http_method':'DELETE'})
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class= serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends =(filters.SearchFilter,)
    search_fields = ('name','email',)
    
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    print(renderer_classes)
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permission.UpdateOwnStatus,
        #IsAuthenticatedOrReadOnly --- for read only permission to unauthentiacate user
        IsAuthenticated
    )
    
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)
    
    
    
    
