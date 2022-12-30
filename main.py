""" Weather app"""

# modules
import flet
from flet import *
import requests
import datetime

api_key = '8d3b0a2d8e81b13ba60923d557f702b2'

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={api_key}')

print(response)