from django.urls import path
from .views import detect_disease, chat, weather_advice

urlpatterns = [
    path('detect-disease/', detect_disease),
    path('chat/', chat),
    path('weather-advice/', weather_advice),
]
