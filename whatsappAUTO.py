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


import time
import webbrowser
try:
    import pyautogui
except:
    speak("I am missing the pyautogui module")
    install("pyautogui")


contactList = {"Enrico": "+27614048752",
               "Mother": "+27732061968"}


def sendwhatmsg(name, message):
    w, h = pyautogui.size()
    webbrowser.open('https://web.whatsapp.com/send?phone='+contactList[name]+'&text='+message)
    time.sleep(19)
    pyautogui.click(x=w/2, y=h/2)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
