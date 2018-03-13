# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from sensor.models import Sensor, SensorData
from sensor.serializers import SensorSerializer, SensorDataSerializer, SensorDetailSerializer


class SensorList(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetail(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorDataList(generics.ListCreateAPIView):
    serializer_class = SensorDataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return SensorData.objects.filter(sensor_id=self.kwargs['sensor_id'])


class SensorDataDetail(generics.RetrieveAPIView):
    serializer_class = SensorDataSerializer

    def get_queryset(self):
        return SensorData.objects.filter(sensor_id=self.kwargs['sensor_id'])