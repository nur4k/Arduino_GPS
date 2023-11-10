from rest_framework.viewsets import ModelViewSet

from main_app.models import Item, Driver
from main_app.serializers import ItemSerializer, DriverSerializer


class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DriverView(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
