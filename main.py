# MODULES -----------------------------------------

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


import os
import random
try:
    import speech_recognition as sr
except:
    speak("I am missing the speechrecognition module")
    install("speechrecognition")
try:
    import randfacts
except:
    speak("I am missing the randfacts module")
    install("randfacts")
import datetime
try:
    import googlesearch
except:
    speak("I am missing the google module")
    install("google")
import webbrowser
try:
    import speedtest
except:
    speak("I am missing the speedtest-cli module")
    install("speedtest-cli")
import time
try:
    import psutil
except:
    speak("I am missing the psutil module")
    install("psutil")
try:
    import wikipedia
except:
    speak("I am missing the wikipedia module")
    install("wikipedia")
# MODULES ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from PC_stats import endProcess
from searchexe import *
from speechLibrary import *
from News import *
from YT_auto import *
from selenium_web import *
from weather2 import *
from uploadToCloud.googleDrive import *
from powerpointpresenting import intro_pres
from whatsappAUTO import *

# from Attendance import name

speak("Importing all preferences from home interface")
from randomJoke import *
speak(joke_validate)

userAccount = getpass.getuser()
print(userAccount)


def writeNote(words):

    fwrite = open("C:\\Users\\"+userAccount+"\\PycharmProjects\\Chaos\\notes.txt", "w")
    fwrite.write(words)
    fwrite.close()


def addToNotes(words):

    fwrite = open("C:\\Users\\"+userAccount+"\\PycharmProjects\\Chaos\\notes.txt", "a")
    fwrite.write(words)
    fwrite.close()


def readNote():

    fread = open("C:\\Users\\"+userAccount+"\\PycharmProjects\\Chaos\\notes.txt", "r")
    contents = fread.read()
    return contents


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + " "

        # return string
    return str1


# speech recognition
r = sr.Recognizer()


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
                searchW = infoSrch[sIndex::]
                print(searchW)

                # speak("Got it Sir, here's what I know about {}".format(searchW))
                speak("Got it Sir, here's what I know")

                speak(wikipedia.summary(searchW,sentences=3))
                text2 = ""
                searchW = ""
                break

            elif "search" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("search")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex::]
                print(searchW)

                speak("Got it")

                link = 'https://www.google.com/search?q={}'.format(searchW)
                webbrowser.open(link)

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
            elif "weather today" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("in")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex::]
                print(searchW)

                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweatherToday(searchW))
                text2 = ""
                continue
            elif "weather tomorrow" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("in")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex::]
                print(searchW)

                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweatherTomorrow(searchW))
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
                st = speedtest.Speedtest()
                speak("Sir the download speed is " + str(int((st.download()/1000)/1000)) + " Megabits per second")
                text2 = ""
                continue
            elif "upload speed" in text2:
                st = speedtest.Speedtest()
                speak("Sir the upload speed is " + str(int((st.upload()/1000)/1000)) + " Megabits per second")
                text2 = ""
                continue
            elif "remind me to" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("to")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex::]
                print(searchW)

                writeNote(listToString(searchW))
                speak("okay, I am done")
                text2 = ""
                continue
            elif "also I need to" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("to")
                sIndex = indexW + 1
                searchW = infoSrch[sIndex::]
                print(searchW)

                addToNotes(" and to "+listToString(searchW))
                speak("okay, I am done")
                text2 = ""
                continue
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
                        speak("Opening {}".format(i))
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
            elif "upload my save game files" in text2:
                speak("I am uploading them now Sir")
                upload_to_drive()
                text2 = ""
                continue
            elif "shutdown" in text2:
                speak("Okay Shutting down")
                os.system('shutdown /s /t 1')
            elif "restart" in text2:
                speak("Okay restarting the system")
                os.system('shutdown /r /t 1')
            elif "logout" in text2:
                speak("Okay logging out sir")
                os.system('shutdown -1')
            elif "present yourself" in text2:
                speak("Sure sir")
                intro_pres()
                text2 = ""
                continue
            elif "tell me" in text2:
                if not (readNote() == ""):
                    speak(random.choice(reminder) + " " + readNote())
                text2 = ""
                continue
            elif "WhatsApp" in text2:
                infoSrch = text2.split()
                indexW = infoSrch.index("WhatsApp")
                sIndex = indexW + 1
                whatppname = infoSrch[sIndex::]
                print(whatppname)
                if whatppname[0] in contactList:
                    speak("what should i say?")
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source)
                        print("listening")
                        audio = r.listen(source)
                        try:
                            textMessage = r.recognize_google(audio)
                            print(textMessage)
                        except:
                            speak("couldn\'t quite catch that")
                            continue
                    sendwhatmsg(whatppname, textMessage)
                    speak("okay, I am done")
                else:
                    speak("This person is not on your contact list")
                text2 = ""
                continue

        except KeyboardInterrupt:
            continue


# timer reminder
timeout = time.time() + 1800  # 1800 secs from now : 30 minutes
timeoutAlarm = time.time() + 0.5
stats_check = time.time() + 0.5  # check starts every one second
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
        elif "clear my reminder" in text:
            speak("I am clearing your reminder")
            writeNote("")
            text = ""
            continue
        elif "sleep" in text:
            if not(readNote() == ""):
                speak(random.choice(reminder) + " " + readNote())
            speak("Okay going to sleep")
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

            if psutil.virtual_memory().percent >= 90.0:
                speak("Sir the system  is using 90 percent of Memory,"
                      " should I terminate the processes causing overload?")
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
                if "yes" in text:
                    speak("Terminating the following programs")
                    endProcess()
                elif "no" in text:
                    speak("Sir this will slow down the computer's performance to undesirable speeds")
            timeoutAlarm = time.time() + 0.5

    except KeyboardInterrupt:
        continue

