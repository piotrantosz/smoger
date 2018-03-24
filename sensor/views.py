# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Sensor


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    sensors = Sensor.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'sensors': sensors},
    )