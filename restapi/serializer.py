"""
Serializer for User and Item Model
All fields are read_only
"""
from login.models import Info
from django.contrib.auth.models import User

from shopping.models import Item
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User Model
    """ 
    phone = serializers.IntegerField(source='info.phone', read_only=True) 
    first_line = serializers.CharField(source='info.first_line', read_only=True) 
    town = serializers.CharField(source='info.town', read_only=True) 
    postcode = serializers.CharField(source='info.postcode', read_only=True)
    
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','phone','first_line','town','postcode')
        read_only_fields = fields
    

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Item Model
    """
    class Meta:
        model = Item
        fields = ('name','price', 'description')
        read_only_fields = fields