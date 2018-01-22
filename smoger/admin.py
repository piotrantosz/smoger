from django.contrib import admin

from .models import Sensor, SensorData


class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'hardware_name']
    search_fields = ['id', 'hardware_name']

    class Meta:
        model = Sensor


class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'lat', 'lon', 'date', 'pm2_5', 'pm10']
    search_fields = ['sensor', 'date']

    class Meta:
        model = SensorData


admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorData, SensorDataAdmin)
