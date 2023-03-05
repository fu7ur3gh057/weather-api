from rest_framework import serializers

from apps.weather.models import Weather, Forecast


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    weather = serializers.CharField(required=False)

    class Meta:
        model = Forecast
        fields = '__all__'


class WeatherForecastListSerializer(serializers.ModelSerializer):
    forecast = ForecastSerializer(many=True)

    class Meta:
        model = Weather
        fields = [
            'location',
            'region',
            'country',
            'latitude',
            'longitude',
            'timezone',
            'local_time',
            'forecast'
        ]
