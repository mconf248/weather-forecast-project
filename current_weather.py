import main_config
import requests
from prettytable import PrettyTable

api_request = requests.get('http://api.weatherstack.com/current?access_key=' + main_config.WEATHERSTACK_API + main_config.WEATHER_ZIPCODE + main_config.WEATHER_UNITS)
if api_request.status_code == 200:
    api_data = api_request.json()

myTable = PrettyTable(["City", "State", "Conditions", "Feels Like (F)", "Precip", "UV Index"])
myTable.align = "c"

weather_descriptions = []
for weather_condition in api_data["current"]["weather_descriptions"]:
    weather_descriptions.append(weather_condition)

myTable.add_row([api_data["location"]["name"], 
                 api_data["location"]["region"], 
                 "".join(weather_descriptions), 
                 api_data["current"]["feelslike"], 
                 api_data["current"]["precip"],
                 api_data["current"]["uv_index"],])

print(myTable)