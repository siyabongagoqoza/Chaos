from selenium import webdriver

import wikipedia
import getpass
import pyttsx3 as p

engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


class infow():
    def __init__(self):
        userAccount = getpass.getuser()
        print(userAccount)
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\' + userAccount + '\\PycharmProjects\\Chaos\\chromedriver\\chromedriver.exe')

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

