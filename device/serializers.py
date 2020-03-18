from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ( 'name', 'type', 'connect', 'currentMode','desireMode','parameter','value','threshold_up','threshold_down','currentState','desireState')