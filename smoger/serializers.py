from rest_framework import serializers
from .models import Sensor, SensorData
from django.shortcuts import get_object_or_404
from .validators import CustomValidation
from rest_framework import status


class SensorDataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate_sensor(self, obj):
        print(self.context)
        sensor = get_object_or_404(Sensor, pk=self.context["view"].kwargs["sensor_id"])
        if sensor.owner != self.context["request"].user:
            raise CustomValidation('Access denied - not owner of sensor', 'sensor',
                                   status_code=status.HTTP_403_FORBIDDEN)
        return sensor

    class Meta:
        model = SensorData
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'hardware_name')


class SensorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'owner', 'hardware_name', 'sensor_data')
