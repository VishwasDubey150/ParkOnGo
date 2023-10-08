from core.models import Locality,Stations,User,Parking,Partner,Local_Business,Reservation
from rest_framework import serializers


class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locality
        fields = '__all__'

class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stations
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class Local_BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local_Business
        fields = '__all__'

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner 
        fields = '__all__'

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'