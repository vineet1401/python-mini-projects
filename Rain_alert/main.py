import requests

MY_API_KEY = "ce7db887d5f3218ed5f31a26e6ea75a2"
MY_LAT = 18.441900
MY_LONG = 73.823631

parameters = {
    "lat":MY_LAT, 
    "lon":MY_LONG,
    "appid":MY_API_KEY
}

response = requests.get(url="https://pro.openweathermap.org/data/2.5/forecast/hourly", params=parameters)
response.raise_for_status()
data = response.json()

print(data)