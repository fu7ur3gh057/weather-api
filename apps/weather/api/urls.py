from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)

from apps.weather.api.views import GetForecastListAPIView, GetCurrentWeather

urlpatterns = [
    path('now/', GetCurrentWeather.as_view(), name='weather'),
    path('forecast/', GetForecastListAPIView.as_view(), name='forecast'),

]
