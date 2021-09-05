import os
import random
import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime
import googlesearch
import webbrowser
import speedtest

from speechLibrary import *
from netflix import *
from News import *
from YT_auto import *
from randomJoke import *
from selenium_web import *
from weather import *

# registering text to speech module
engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')

st = speedtest.Speedtest()


def writeNote(words):

    fwrite = open("notes.txt", "w")
    fwrite.write(words)
    fwrite.close()


def readNote():

    fread = open("notes.txt", "r")
    contents = fread.read()
    return contents


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


today_date = datetime.datetime.now()
timeOfDay = today_date.strftime("%p")
dayTime24 = int(today_date.strftime("%H"))
# speech recognition
r = sr.Recognizer()

if timeOfDay == "AM":
    speak("Good morning sir, how can I help?")

if 12 <= dayTime24 <= 17:
    speak("Good Afternoon sir, how can I help?")

if 18 <= dayTime24 <= 23:
    speak("Good evening sir, how can I help?")


# listens for commands
def listen():
    text2 = ""
    while True:
        print(text2)
        try:
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source)
                print("listening")
                audio = r.listen(source)
                try:
                    text2 = r.recognize_google(audio)
                    print(text2)
                except:
                    continue

            if "information" in text2:
                speak("what would you like to know")

                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source)
                    print("listening")
                    audio = r.listen(source)
                    try:
                        topic = r.recognize_google(audio)
                        print(topic)
                    except:
                        speak("couldn\'t quite catch that")
                        continue

                speak("searching {} in wikipedia".format(topic))
                assist = infow()
                assist.get_info(topic)
                speak(assist.summarize(topic))
                text2 = ""
                break

            elif "search" in text2:
                speak("what would you like to search?")
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source)
                    print("listening")
                    audio = r.listen(source)
                    try:
                        query = r.recognize_google(audio)
                        print(query)
                    except:
                        speak("couldn\'t quite catch that")
                        continue
                for j in googlesearch.search(query, tld='com', lang='en', num=1, stop=1, pause=2.0):
                    print(j)
                    webbrowser.open(j)
                text2 = ""
                continue

            elif "YouTube" in text2:
                speak(random.choice(playOnYoutube1))
                text2 = ""
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, 1.2)
                    print("listening")
                    audio = r.listen(source)
                    try:
                        text2 = r.recognize_google(audio)
                        print(text2)
                    except:
                        speak("couldn\'t quite catch that")
                        continue
                    speak(random.choice(playOnYoutube2).format(text2))
                    assist = music()
                    assist.play(text2)
                    text2 = ""
                    break

            elif "news" in text2:
                speak(random.choice(newsRead))
                arr = news()
                for i in range(len(arr)):
                    speak(arr[i])

            elif "fact" in text2:
                speak("Got it, one random fact coming up")
                x = randfacts.getFact()
                print(x)
                speak("did you know that" + x)
                text2 = ""
                continue

            elif "joke" in text2:
                speak("Sure sir, get ready for some humor")
                joke()
                for i in range(len(arrJ)):
                    print(arrJ[i])
                    speak(arrJ[i])
                text2 = ""
                continue
            elif "date today" in text2:
                speak("today is the " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y"))
                text2 = ""
                continue
            elif "day is it" in text2:
                speak("today is" + today_date.strftime("%A"))
                text2 = ""
                continue
            elif "time" in text2:
                speak("It is " + today_date.strftime("%I") + " " + today_date.strftime("%M") + today_date.strftime("%p"))
                text2 = ""
                continue
            elif "weather" in text2:
                speak("the temperature in pretoria is " + str(temp()) + " degrees celsius, with " + des() + "...")
                text2 = ""
                continue
            elif "sick beats" in text2:
                speak(random.choice(playSickBeats))
                webbrowser.open("https://www.youtube.com/watch?v=wLoWd2KyUro&list=PLR5Cmjo90BNguiSb2wDShPdKoa-Xiw5x1")
                text2 = ""
                break
            elif "chill music" in text2:
                speak(random.choice(playChillMusic))
                webbrowser.open("https://www.youtube.com/watch?v=NxSDNogkKX0")
                text2 = ""
            elif "download speed" in text2:
                speak("Sir the download speed is " + str(st.download()))
                text2 = ""
                continue
            elif "upload speed" in text2:
                speak("Sir the upload speed is " + str(st.upload()))
                text2 = ""
                continue
            elif "write" in text2:
                speak("what should I write?")
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source)
                    print("listening")
                    audio = r.listen(source)
                    try:
                        text2 = r.recognize_google(audio)
                        print(text)
                    except:
                        speak("couldn\'t catch that sir")
                        continue
                speak("okay, I am done")
                writeNote(text2)
                text2 = ""
                continue
            elif "Netflix" in text2:
                speak(random.choice(openNetflix))
                assist = movies()
                assist.wNetflix()
                text2 = ""
                break
            elif "who are you" in text2:
                speak(random.choice(introduction))

            elif "thanks" in text2:
                speak("Happy to help")
                text2 = ""
                break
            elif "steam" in text2:
                os.system("C:/Program\ Files\ (x86)/Steam/steam.exe")

        except KeyboardInterrupt:
            break


# listens for its name to accept commands
text = ""
while True:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source)
        print("listening")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            continue

    if "chaos" in text:
        speak(random.choice(respondToWake))
        listen()
        text = ""

    if "sleep" in text:
        if not(readNote() == ""):
            speak(random.choice(reminder) + " " + readNote())
        speak("Okay shutting down")

        break
