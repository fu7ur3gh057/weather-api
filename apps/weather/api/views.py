import os

import requests
from dotenv import load_dotenv
from requests import Response as ReqResponse
from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *

load_dotenv()


def make_api_request(url: str, data: dict) -> ReqResponse:
    ''' Call request yo M30 RestAPI service, return request.Response '''
    api_token = os.environ.get('M3O_API_TOKEN', '')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_token
    }
    response = requests.post(url, headers=headers, json=data)
    return response


class GetCurrentWeather(views.APIView):
    '''
    View class for getting current weather by location,
    body arguments: location: str
     '''
    serializer_class = WeatherSerializer

    def get(self, request: Request):
        url = 'https://api.m3o.com/v1/weather/Now'
        location = request.data['location']
        data = {"location": location}
        response = make_api_request(url=url, data=data)
        if response.status_code == 200:
            serializer = self.serializer_class(data=response.json())
            if serializer.is_valid(raise_exception=True):
                return Response(serializer.data)
        else:
            return Response({response.text})


class GetForecastListAPIView(views.APIView):
    '''
    View class for getting forcast weather by location and days,
    body arguments: days: int, location: str
     '''
    serializer_class = WeatherForecastListSerializer

    def get(self, request: Request):
        url = 'https://api.m3o.com/v1/weather/Forecast'
        days = request.data['days']
        location = request.data['location']
        data = {'days': days, 'location': f'{location}'}
        response = make_api_request(url=url, data=data)
        if response.status_code == 200:
            serializer = self.serializer_class(data=response.json())
            if serializer.is_valid(raise_exception=True):
                return Response(serializer.data)
        else:
            return Response({response.text})
