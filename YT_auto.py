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
    from selenium import webdriver
except:
    speak("I am missing the selenium module")
    install("selenium")

import getpass


class music():
    def __init__(self):
        userAccount = getpass.getuser()
        print(userAccount)
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\'+ userAccount +'\\PycharmProjects\\Chaos\\chromedriver\\chromedriver.exe')

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]')
        video.click()
