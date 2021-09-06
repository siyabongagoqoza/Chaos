from selenium import webdriver
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
