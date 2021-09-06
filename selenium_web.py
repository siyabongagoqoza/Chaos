from selenium import webdriver

import wikipedia
import getpass

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
        results = wikipedia.summary(query, sentences=2)
        print(results)
        return results



