import requests
from pprint import pprint

API_Key = "ca3855b6e00b775c97cb08b0b91b5e5f"

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/3.0/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)