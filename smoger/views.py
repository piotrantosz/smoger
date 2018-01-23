# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from smoger.models import Sensor, SensorData
from smoger.serializers import SensorSerializer, SensorDataSerializer, SensorDetailSerializer