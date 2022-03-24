import subprocess
import sys
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

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
def install(package):
    speak("Installing the {} module, you may need to restart my process after the installation".format(package))
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# install("pywin32")
