import pyttsx3 as p

# registering text to speech module FIRST
engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


try:
    import requests
except:
    speak("I am missing the requests module")
from apiKeys import *

url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
querystring = {"lat": "-33.918861", "lng": "18.423300"}
headers = {
    'x-api-key': ambeeWeatherKey,
    'Content-type': "application/json"
    }
response = requests.request("GET", url, headers=headers, params=querystring).json()

celsiusTemp = int((((response["data"]["apparentTemperature"]) - 32) * 5/9))
# print(int(celsiusTemp))
summary = response["data"]["summary"]
# print(summary)


comment = ""
if 16 <= celsiusTemp <= 19:
    comment = "Carry a hoodie or jacket sir just in case."

if 0 <= celsiusTemp <= 15:
    comment = "Wear something warm sir It will be chilly"

if celsiusTemp >= 20:
    comment = "Take sunglasses with you sir"

description = "Today in Cape Town it is " + str(celsiusTemp) + " degrees celsius and " + summary + ". " + comment
