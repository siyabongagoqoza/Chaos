import os
import random
import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime
import googlesearch
import webbrowser
import speedtest
import time

from searchexe import *
from speechLibrary import *
from netflix import *
from News import *
from YT_auto import *
from selenium_web import *
from weather import *


# registering text to speech module
engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


from Attendance import name

speak("Importing all preferences from home interface")
from randomJoke import *
speak(joke_validate)
st = speedtest.Speedtest()
userAccount = getpass.getuser()
print(userAccount)


def writeNote(words):

    fwrite = open("C:\\Users\\"+userAccount+"\\PycharmProjects\\Chaos\\notes.txt", "w")
    fwrite.write(words)
    fwrite.close()


def readNote():

    fread = open("C:\\Users\\"+userAccount+"\\PycharmProjects\\Chaos\\notes.txt", "r")
    contents = fread.read()
    return contents


def addToNote(words):
    fadd = open("notes.txt", "a")
    fadd.append(words)
    fadd.close()


# speech recognition
r = sr.Recognizer()

userAccount = getpass.getuser()
print(userAccount)
# timer reminder
timeout = time.time() + 1800  # 1800 secs from now : 30 minutes
timeoutAlarm = time.time() + 1


# listens for commands
def listen():
    text2 = ""
    while True:
        print(text2)
        today_date = datetime.datetime.now()

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
                infoSrch = text2.split()
                indexW = infoSrch.index("about")
                sIndex = indexW + 1
                try:
                    searchW = infoSrch[sIndex] + " " + infoSrch[sIndex+1]
                    print(searchW)
                except:
                    searchW = infoSrch[sIndex]
                    print(searchW)

                # speak("Got it Sir, here's what I know about {}".format(searchW))
                speak("Got it Sir, here's what I know")

                assist = infow()
                assist.get_info(searchW)
                speak(assist.summarize(searchW))
                text2 = ""
                searchW = ""
                break

            elif "search" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("search")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex]
                print(searchW)

                speak("Got it")

                for j in googlesearch.search(searchW, tld='com', lang='en', num=1, stop=1, pause=2.0):
                    print(j)
                    webbrowser.open(j)

                text2 = ""
                searchW = ""
                continue

            elif "YouTube" in text2:
                speak(random.choice(playOnYoutube1))
                text2 = ""
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source)
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
                speak("Sure sir")
                the_joke = getJoke()
                for i in range(len(the_joke)):
                    speak(the_joke[i])
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
                speak(description)
                text2 = ""
                continue
            elif "be cold" in text2:
                if celsiusTemp <= 16:
                    speak("Yes it will Sir" + ", I would suggest you " + comment)
                if 17 <= celsiusTemp <= 20:
                    speak("It will be a bit warm Sir" + ", I would suggest you " + comment)
                if 21 <= celsiusTemp:
                    speak("It will be hot" + ", I would suggest you " + comment)
                text2 = ""
                continue
            elif "be warm" in text2:
                if celsiusTemp <= 16:
                    speak("No sir it will be cold" + ", I would suggest you " + comment)
                if 17 <= celsiusTemp <= 20:
                    speak("Yes Sir" + ", I would suggest you " + comment)
                if 21 <= celsiusTemp:
                    speak("Yes will be hot in fact" + ", I would suggest you " + comment)
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
                break
            elif "download speed" in text2:
                speak("Sir the download speed is " + str(int(st.download())))
                text2 = ""
                continue
            elif "upload speed" in text2:
                speak("Sir the upload speed is " + str(int(st.upload())))
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
                text2 = ""
                continue
            elif "thanks" in text2:
                speak("Happy to help")
                text2 = ""
                break
            elif "open" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("open")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex]
                print(searchW)
                scanFiles()
                for i in addToDict:
                    if searchW in i:
                        os.startfile(addToDict[searchW])
                        print(i)
                text2 = ""
                searchW = ""
                break
            elif "volume" in text2:
                speak(random.choice(volumeSpeak))
                import volumeHandControl
                text2 = ""
                continue
            elif "virtual Mouse" in text2:

                speak("going to virtual mode")
                import VirtualMouse
                text2 = ""
                continue

        except KeyboardInterrupt:
            continue


speak("System is now fully operational")
# listens for its name to accept commands
text = ""
test = 0
while True:
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source)
            print("listening")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
            except:
                pass
        # check time for alarm
        today_date_alarm = datetime.datetime.now()
        if "chaos" in text:
            speak(random.choice(respondToWake))
            listen()
            text = ""

        elif "sleep" in text:
            if not(readNote() == ""):
                speak(random.choice(reminder) + " " + readNote())
            speak("Okay shutting down")
            break
        elif "standby" in text:
            speak("okay Sir")
            text = ""
        elif "who are you" in text:
            speak(random.choice(introduction))
            text = ""
        # reminder
        elif time.time() > timeout:
            speak(random.choice(reminder) + " " + readNote())
            timeout = timeout + 1800  # refreshes the reminder timer for another 30 min

        elif time.time() > timeoutAlarm:
            if today_date_alarm.strftime("%I") == "12" and today_date_alarm.strftime("%M") == "00":
                speak("It is lunch time Sir")

        elif "who are you" in text:
            speak(random.choice(introduction))
            text2 = ""
    except KeyboardInterrupt:
        continue

