# Cookies created for login process

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


    def quit(self):
        self.driver.quit()

    def login(self):
        username_input = self.driver.find_element(by=By.NAME, value="user-name")
        password_input = self.driver.find_element(by=By.NAME, value="password")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")

        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(5)

    def getTitle(self):
        return self.driver.title

    def getCurrentURL(self):
        return self.driver.current_url


    def getCookies(self):
        return self.driver.get_cookies()



url = "https://www.saucedemo.com/"

obj = LoginPage(url)
obj.boot()
print(obj.getCookies())
obj.login()
#print(obj.getCurrentURL())
current_url = obj.getCurrentURL()
print("Current URL of the webpage:", current_url)
#print(obj.getTitle())
title = obj.getTitle()
print("Title of the webpage:", title)
print(obj.getCookies())
obj.quit()

