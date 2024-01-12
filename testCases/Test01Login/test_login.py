import pytest
from selenium import webdriver

from pages.login.login_page import loginPage
from pages.homepage.home_page import homePage


class TestLogin():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        print("111111111111111")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://gpmuat.midea.com/')
        self.loginpage = loginPage(self.driver)

    def test_login_success(self):
        self.loginpage.login('caizq20','caizq@20')

    @pytest.mark.skip
    def test_logOut_success(self):
        self.loginpage.logout()

    @pytest.mark.parametrize('userName',['liuww1'])
    def test_simulateLogin(self,userName):
        print("22222222222222")
        self.loginpage.simulateLogin(userName)




    def teardown_class(self):
        pass