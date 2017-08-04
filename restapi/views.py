from login.models import User
from shopping.models import Item
from rest_framework import viewsets
from restapi.serializer import UserSerializer, ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for the User model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    Viewset for the Item model
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer