import getpass
import os
import time

import pyttsx3 as p

# registering text to speech module FIRST

engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')

import win32com.client
from speechLibrary import *


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


userAccount = getpass.getuser()
print(userAccount)


def intro_pres():
    os.startfile('C:\\Users\\'+userAccount+'\\PycharmProjects\\Chaos\\pptx\\CHAOS.pptx')
    time.sleep(1)
    app = win32com.client.GetActiveObject("PowerPoint.Application")
    pptpres = app.ActivePresentation
    pptpres.SlideShowSettings.Run()
    time.sleep(3)
    speak(presentation1)
    time.sleep(2)
    pptpres.SlideShowWindow.View.Next()
    time.sleep(0.5)
    speak(presentation2)


# intro_pres()


