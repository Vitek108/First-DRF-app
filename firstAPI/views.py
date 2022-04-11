from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from firstAPI.models import Car, Fleet
from firstAPI.serializers import FleetSerializer, CarDetailSerializer, CarListSerializer
import random
import string


# class CarViewSet(ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):  # odlišné zobrazení pro Detail a List
        if self.action == 'retrieve':
            return CarDetailSerializer
        else:
            return CarListSerializer

    def perform_create(self, serializer):
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        serializer.save(signature_code=code)


class FleetViewSet(ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
