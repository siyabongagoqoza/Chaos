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
    import python_weather
except:
    speak("I am missing the module python_weather")
    install("python_weather")
import asyncio
import datetime


async def getweatherToday(query):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    weather = await client.find(query)

    print(weather.current.temperature)

    date_today = str(datetime.datetime.today())
    date_compare = date_today.split()
    print(date_compare[0])

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)
        if (date_compare[0] + " 00:00:00") == str(forecast.date):
            print("yes")
            if weather.current.temperature <= 16:
                comment = "Sir it is " + str(
                    weather.current.temperature) + " degrees celsius and it is " + forecast.sky_text + ", please wear something warm"
                speak(comment)
            if 17 <= weather.current.temperature <= 20:
                comment = "Sir it is " + str(
                    weather.current.temperature) + " degrees celsius and it is " + forecast.sky_text + ", take a jacket or hoodie with you just in case"
                speak(comment)
            if 21 <= weather.current.temperature <= 30:
                comment = "Sir it is " + str(
                    weather.current.temperature) + " degrees celsius and it is " + forecast.sky_text + ", Wear sunglasses"
                speak(comment)
    await client.close()


async def getweatherTomorrow(query):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    weather = await client.find(query)

    print(weather.current.temperature)

    date_tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)
        if (date_tomorrow + " 00:00:00") == str(forecast.date):
            print("yes")
            if forecast.temperature <= 16:
                comment = "Sir Tomorrow it will be " + str(forecast.temperature) + " degrees celsius and it will be " + forecast.sky_text + ", please wear something warm"
                speak(comment)
            if 17 <= forecast.temperature <= 20:
                comment = "Sir Tomorrow it will be " + str(forecast.temperature) + " degrees celsius and it will be " + forecast.sky_text + ", take a jacket or hoodie with you just in case"
                speak(comment)
            if 21 <= forecast.temperature <= 30:
                comment = "Sir Tomorrow it will be " + str(forecast.temperature) + " degrees celsius and it will be " + forecast.sky_text + ", Wear sunglasses"
                speak(comment)
    await client.close()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(getweatherToday("cape town"))
# loop.run_until_complete(getweatherTomorrow("cape town"))
