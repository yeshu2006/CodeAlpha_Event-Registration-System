from rest_framework import serializers
from .models import Event, Registration


class EventSerializer(serializers.ModelSerializer):
    available_tickets = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        extra_fields = ['available_tickets']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
