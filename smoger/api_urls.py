from django.urls import path
from smoger import views
from django.conf.urls import include


urlpatterns = [
    path('sensors/', views.SensorList.as_view()),
    path('sensors/<int:pk>/', views.SensorDetail.as_view()),
    path('sensors/<int:sensor_id>/data/', views.SensorDataList.as_view()),
    path('sensors/<int:sensor_id>/data/<int:pk>/', views.SensorDataDetail.as_view()),
    path('auth/', include('rest_framework.urls')),
]
