from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from .models import Vehicle, Driver, Route, VehicleStatus
from .serializers import VehicleSerializer, DriverSerializer, RouteSerializer, RegisterSerializer, \
    VehicleStatusSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class VehicleStatusViewSet(viewsets.ModelViewSet):
    queryset = VehicleStatus.objects.all()
    serializer_class = VehicleStatusSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
