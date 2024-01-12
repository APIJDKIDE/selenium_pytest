from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

class Test_ActionChains():

    def setup_method(self):


        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def test_move(self):
        ele = self.driver.find_element(By.ID,'s-top-loginbtn').click()
        print("aaaaaaaaaaa")
        sleep(10)

    def teardown_method(self):

        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-v','-s','canDelete.py'])
