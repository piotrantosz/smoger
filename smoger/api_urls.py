from django.urls import path
from smoger import api_views
from django.conf.urls import include


urlpatterns = [
    path('sensors/', api_views.SensorList.as_view()),
    path('sensors/<int:pk>/', api_views.SensorDetail.as_view()),
    path('sensors/<int:sensor_id>/data/', api_views.SensorDataList.as_view()),
    path('sensors/<int:sensor_id>/data/<int:pk>/', api_views.SensorDataDetail.as_view()),
    path('auth/', include('rest_framework.urls')),
]
