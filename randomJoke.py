import pyttsx3 as p
from installMissingModules import *
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
    speak("I am missing the requests modules")
    install("requests")

try:
    joke_validate = ""


    def getJoke():

        url = "https://v2.jokeapi.dev/joke/Any?type=twopart&safemode"
        json_data = requests.get(url).json()

        arrJ = ["",""]
        arrJ[0] = json_data["setup"]
        arrJ[1] = json_data["delivery"]
        return arrJ

except:
    joke_validate = "Jokes are not available"
