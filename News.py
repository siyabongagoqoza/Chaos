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

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + key
json_data = requests.get(api_address).json()

ar = []


def news():
    for i in range(3):
        ar.append("Number " + str(i+1) + ", " + json_data["articles"][i]["title"] + ".")

    return ar


