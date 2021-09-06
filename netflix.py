import getpass

from selenium import webdriver


class movies():
    def __init__(self):
        userAccount = getpass.getuser()
        print(userAccount)
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\'+userAccount+'\\PycharmProjects\\CHAOS\\chromedriver\\chromedriver.exe')

    def wNetflix(self):
        self.driver.get(url="https://www.netflix.com/za/login")
        opener = self.driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/label')
        opener.click()
        username = self.driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
        username.click()
        username.send_keys('siyabongagoqoza@gmail.com')
        password = self.driver.find_element_by_xpath('//*[@id="id_password"]')
        password.click()
        password.send_keys('$iyabonga99')
        enter = self.driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        enter.click()
        profile = self.driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div')
        profile.click()



