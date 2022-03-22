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
try:
    import wikipedia
except:
    speak("I am missing the wikipedia module")
    install("wikipedia")
import getpass


class infow():
    def __init__(self):
        userAccount = getpass.getuser()
        print(userAccount)
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\' + userAccount + '\\Chaos\\chromedriver\\chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.com")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

    def summarize(self, query):
        try:
            results = wikipedia.summary(query, sentences=2)
            print(results)
            return results
        except:
            speak("Sir the term " + query + " can refer to various titles, "
                                            "a more specific query will suffice")
            pass

# assist = infow()
# assist.get_info("Iris")
# print(assist.summarize("lollipop"))

