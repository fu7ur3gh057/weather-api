from django.db import models


class Weather(models.Model):
    location = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timezone = models.CharField(max_length=100)
    local_time = models.DateTimeField()
    # nullable
    temp_c = models.IntegerField(null=True)
    temp_f = models.FloatField(null=True)
    feels_like_c = models.FloatField(null=True)
    humidity = models.IntegerField(null=True)
    cloud = models.IntegerField(null=True)
    daytime = models.BooleanField(null=True)
    condition = models.CharField(null=True, max_length=255)
    icon_url = models.CharField(null=True, max_length=255)
    wind_mph = models.FloatField(null=True)
    wind_kph = models.FloatField(null=True)
    wind_direction = models.CharField(null=True, max_length=255)
    wind_degree = models.IntegerField(null=True)


class Forecast(models.Model):
    weather = models.ForeignKey(Weather, related_name='forecasts', on_delete=models.CASCADE)
    date = models.DateTimeField()
    max_temp_c = models.FloatField()
    max_temp_f = models.FloatField()
    min_temp_c = models.FloatField()
    min_temp_f = models.FloatField()
    avg_temp_c = models.FloatField()
    avg_temp_f = models.FloatField()
    will_it_rain = models.BooleanField(default=False)
    chance_of_rain = models.IntegerField()
    condition = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=255)
    sunrise = models.CharField(max_length=100)
    sunset = models.CharField(max_length=100)
    max_wind_mph = models.FloatField()
    max_wind_kph = models.FloatField()
