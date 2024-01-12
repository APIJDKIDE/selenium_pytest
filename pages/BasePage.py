from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class basePage():

    def __init__(self,driver:webdriver):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)
    def finds(self,locator):
        return self.driver.find_elements(*locator)






