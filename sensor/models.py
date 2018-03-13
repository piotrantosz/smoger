# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid
from django.utils import timezone
import os


def generate_path(instance, filename):
    name, extension = os.path.splitext(filename)
    return '{0}/{1}{2}'.format(instance.sensor.id, instance.date, extension)


class Sensor(models.Model):
    owner = models.ForeignKey('auth.User', related_name='sensor', on_delete=models.CASCADE)
    hardware_name = models.CharField(max_length=120)

    def __unicode__(self):
        return '{0}-{1}'.format(self.id, self.hardware_name)

    def __str__(self):
        return '{0}-{1}'.format(self.id, self.hardware_name)


class SensorData(models.Model):
    sensor = models.ForeignKey('Sensor', null=True, blank=True, on_delete=models.CASCADE, related_name='sensor_data')
    date = models.DateTimeField(default=timezone.now, blank=True)
    pm2_5 = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    pm10 = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    pressure = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=1)
    temperature = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=1)
    lat = models.FloatField(blank=False, null=False)
    lon = models.FloatField(blank=False, null=False)
    picture = models.ImageField(upload_to=generate_path, blank=True, null=True)

    def __unicode__(self):
        return '{0}-{1}'.format(self.sensor, self.date)

    def __str__(self):
        return '{0}-{1}'.format(self.sensor, self.date)

    class Meta:
        ordering = ["-date"]
