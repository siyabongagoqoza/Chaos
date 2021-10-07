import datetime
import json
from installMissingModules import *
import pyttsx3 as p

# registering text to speech module FIRST

engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 127)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


try:
    import requests
except:
    speak("I am missing the requests module")
    install('requests')


def retrieve_messages(channelid):
    headers = {
        'authorization': 'Njk0NDg2MDE2MDE0NDE3OTcw.YV6YdQ.yx9Ff5CFSe_O6m_TMC6-gTc-4c4'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=5', headers=headers)
    countMsg = 0
    jsonn = json.loads(r.text)
    for value in jsonn:
        msgDate = value['timestamp'][:10]
        # print(msgDate)
        if msgDate == str(datetime.date.today()):
            print(value['author']['username'] + ": " + value['content'], msgDate, '\n')
            countMsg += 1
    if countMsg > 0:
        speak("You have new messages")
    else:
        speak("No new messages")


ninetailsofpogLookingforfriendly = '863296196948787240'
# retrieve_messages(ninetailsofpogLookingforfriendly)

