from time import sleep

from selenium.webdriver import ActionChains

from pages.BasePage import basePage
from pages.login.login_page_locator import loginPageLocator as LPL


class loginPage(basePage):


    #登录成功
    def login(self,userName,passWord):

        self.find(LPL.userAgreement).click()
        self.find(LPL.userName).send_keys(userName)
        self.find(LPL.passWord).send_keys(passWord)
        self.find(LPL.login).click()


    def logout(self):
        ele = self.find(LPL.currentUsername)
        ActionChains(self.driver).move_to_element(ele).perform()
        sleep(5)
        self.find(LPL.logOut).click()

    def simulateLogin(self,userName):
        ele = self.find(LPL.currentUsername)
        ActionChains(self.driver).move_to_element(ele).perform()
        sleep(3)
        self.find(LPL.simulate).click()
        sleep(3)
        self.find(LPL.inputUserName).sendKeys(userName)
        sleep(3)
        self.find(LPL.searchButton).click()
        sleep(3)
        self.finds(LPL.searchResults)[0].click()  #点击第一个搜索结果
        sleep(3)
        self.find(LPL.selectUser).click()