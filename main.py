import pyttsx3 as p
import speech_recognition as    sr
import randfacts
import datetime
import googlesearch
import webbrowser


from News import *
from YT_auto import *
from randomJoke import *
from selenium_web import *
from weather import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voice = engine.getProperty('voice')


def speak(text):
    engine.say(text)
    engine.runAndWait()


today_date = datetime.datetime.now()
timeOfDay = today_date.strftime("%p")
dayTime24 = int(today_date.strftime("%H"))
# speech recognition
r = sr.Recognizer()

if timeOfDay == "AM":
    print("Good morning sir, how can I help?")
    speak("Good morning sir, how can I help?")

if 12 <= dayTime24 <= 17:
    print("Good Afternoon sir, how can I help?")
    speak("Good Afternoon sir, how can I help?")

if 18 <= dayTime24 <= 23:
    print("Good evening sir, how can I help?")
    speak("Good evening sir, how can I help?")


# listens for commands
def listen():
    text2 = ""
    while True:
        print(text2)
        try:
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
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
                    r.adjust_for_ambient_noise(source, 1.2)
                    print("listening")
                    audio = r.listen(source)
                    try:
                        topic = r.recognize_google(audio)
                        print(topic)
                    except:
                        speak("couldn\'t quite catch that")

                speak("searching {} in wikipedia".format(topic))
                print("searching {} in wikipedia".format(topic))
                assist = infow()
                assist.get_info(topic)
                text2 = ""
                continue

            elif "search" in text2:
                print("what would you like to search?")
                speak("what would you like to search?")
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, 1.2)
                    print("listening")
                    audio = r.listen(source)
                    try:
                        query = r.recognize_google(audio)
                        print(query)
                    except:
                        continue
                for j in googlesearch.search(query, tld='com', lang='en', num=1, stop=1, pause=2.0):
                    print(j)
                    webbrowser.open(j)
                text2 = ""
                continue

            elif "play" and "video" in text2:
                speak("Which video should i play for you?")
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
                    speak("playing {} on youtube".format(text2))
                    print("playing {} on youtube".format(text2))
                    assist = music()
                    assist.play(text2)
                    text2 = ""
                    break

            elif "news" in text2:
                print("Sure sir these are the top headlines,")
                speak("Sure sir these are the top headlines,")
                arr = news()
                for i in range(len(arr)):
                    speak(arr[i])
                    print(arr[i])

            elif "fact" in text2:
                print("Got it, one random fact coming up")
                speak("Got it, one random fact coming up")
                x = randfacts.getFact()
                print(x)
                speak("did you know that" + x)
                text2 = ""
                continue

            elif "joke" in text2:
                print("Sure sir, get ready for some humor")
                speak("Sure sir, get ready for some humor")
                joke()
                for i in range(len(arrJ)):
                    print(arrJ[i])
                    speak(arrJ[i])
                text2 = ""
                continue
            elif "date today" in text2:
                print("today is the " + today_date.strftime("%d") + " of " + today_date.strftime(
                    "%B") + " " + today_date.strftime("%Y"))
                speak("today is the " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " " + today_date.strftime("%Y"))
                text2 = ""
                continue
            elif "day is it" in text2:
                print("today is" + today_date.strftime("%A"))
                speak("today is" + today_date.strftime("%A"))
                text2 = ""
                continue
            elif "time" in text2:
                print("It is " + today_date.strftime("%I") + " " + today_date.strftime("%M") + today_date.strftime("%p"))
                speak("It is " + today_date.strftime("%I") + " " + today_date.strftime("%M") + today_date.strftime("%p"))
                text2 = ""
                continue
            elif "weather" in text2:
                print("the temperature in pretoria is " + str(temp()) + " degrees celsius, with " + des() + "...")
                speak("the temperature is pretoria is " + str(temp()) + " degrees celsius, with " + des() + "...")
                text2 = ""
                continue
            elif "sick beats" in text2:
                print("playing sick beats")
                webbrowser.open('https://www.youtube.com/watch?v=wLoWd2KyUro&list=PLR5Cmjo90BNguiSb2wDShPdKoa-Xiw5x1')
                text2 = ""
                break
            elif "thanks" in text2:
                print("Happy to help")
                speak("Happy to help")
                text2 = ""
                break

        except KeyboardInterrupt:
            break


# listens for its name to accept commands
text = ""
while True:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            continue

    if "chaos" in text:
        print("Yes sir?")
        speak("Yes sir?")
        listen()
        text = ""
