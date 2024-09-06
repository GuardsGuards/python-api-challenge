import datetime as dt
import requests

base_url = "http://openweathermap.org/data/2.5/weather?"
api_key = "b2a2690c2eee9506586af1ae69c9822d"
city = "London"


url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

print(response)
