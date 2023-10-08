from django.shortcuts import render
from .serializers import LocalitySerializer,UserSerializer,ParkingSerializer,PartnerSerializer,Local_BusinessSerializer,StationSerializer,ReservationSerializer
from core.models import Locality,User,Parking,Partner,Local_Business,Stations,Reservation
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class Local_BusinessViewSet(viewsets.ModelViewSet):
    queryset = Local_Business.objects.all()
    serializer_class = Local_BusinessSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Stations.objects.all()
    serializer_class = StationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
