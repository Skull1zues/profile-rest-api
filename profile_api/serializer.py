from rest_framework import serializers
from profile_api import models


class HelloSerializers(serializers.Serializer):
    """Serializers a name field for testing APIVIEW"""
    name=serializers.CharField(max_length=10)
    
