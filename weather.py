import requests

from apiKeys import *

url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
querystring = {"lat": "-33.918861", "lng": "18.423300"}
headers = {
    'x-api-key': ambeeWeatherKey,
    'Content-type': "application/json"
    }
response = requests.request("GET", url, headers=headers, params=querystring).json()

celsiusTemp = int((((response["data"]["apparentTemperature"]) - 32) * 5/9))
#print(int(celsiusTemp))
summary = response["data"]["summary"]
#print(summary)


comment = ""
if 16 <= celsiusTemp <= 19:
    comment = "Carry a hoodie or jacket sir just in case."

if 0 <= celsiusTemp <= 15:
    comment = "Wear something warm sir It will be chilly"

if celsiusTemp >= 20:
    comment = "Take sunglasses with you sir"

description = "Today in Cape Town it is " + str(celsiusTemp) + " degrees celsius and " + summary + ". " + comment
