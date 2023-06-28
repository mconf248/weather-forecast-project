#Simple script to obtain weather information from WeatherStack API

import main_config
import requests
import table_config

r = requests.get('http://api.weatherstack.com/current?access_key='+ main_config.WEATHERSTACK_API +'&query='+ main_config.WEATHER_ZIPCODE +'')
data = r.json()
print(data)
