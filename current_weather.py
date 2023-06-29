#Simple script to obtain weather information from WeatherStack API

import main_config
import requests
from prettytable import PrettyTable

api_request = requests.get('http://api.weatherstack.com/current?access_key='+ main_config.WEATHERSTACK_API +'&query='+ main_config.WEATHER_ZIPCODE +'')
api_data = api_request.json()

myTable = PrettyTable(["City", "State", "Conditions", "Feels Like (C)", "Temperature (C)"])
myTable.align = "c"

weather_descriptions = []
for element in api_data["current"]["weather_descriptions"]:
    weather_descriptions.append(element)

myTable.add_row([api_data["location"]["name"], api_data["location"]["region"], ", ".join(weather_descriptions) ,api_data["current"]["feelslike"],api_data["current"]["temperature"] ])
print(myTable)