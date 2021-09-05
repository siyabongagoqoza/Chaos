from selenium import webdriver


class google_sign_in():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\Cash\\PycharmProjects\\CHAOS\\chromedriver\\chromedriver.exe')

    def sign_in(self):
        self.driver.get(url="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAmgQ")
        username = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        username.click()
        username.send_keys('siyabongagoqoza@gmail.com')
        userbutton = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        userbutton.click()
        password = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.click()
        password.send_keys('clerence')
        enter = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        enter.click()


assist = google_sign_in()
assist.sign_in()
