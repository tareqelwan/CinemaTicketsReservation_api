from rest_framework import  serializers
from tickets.models import Guest,Reservation,Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields= '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields=['pk','reservation','name','mobile'] # for demo, should use => uuid or slug

