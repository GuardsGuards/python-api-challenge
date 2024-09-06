import matplotlib.pyplot as plt
import requests
import pandas as pd
api_key = "b2a2690c2eee9506586af1ae69c9822d"
url = "http://api.openweathermap.org/data/3.0/onecall?"
units = "metric"
query_url = f"{url}appid={api_key}&units={units}&q="
cities = ["Washington DC", "Charlotte"]
lat = []
temp = []
for city in cities:
    response = requests.get(query_url + city).json()
    lat.append(response['coord']['lat'])
    temp.append(response['main']['temp'])
print(f"The latitude information recieved is: {lat}")
print(f"The temperature information recieved is: {temp}")
weather_dict = {
    "cities": cities,
    "lat": lat,
    "temp": temp
}
weather_data = pd.DataFrame(weather_dict)
plt.scatter(weather_data["lat"], weather_data["temp"], marker="o")
