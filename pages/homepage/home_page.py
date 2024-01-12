import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from pages.BasePage import basePage
from pages.homepage.home_page_locator import homePageLocator as HPL



class homePage(basePage):

    # 点击GPM的Logo
    def goto_homePage(self):
        self.find(HPL.logo).click()

    # 模拟登录
    def simulationLogin(self,userName):
        time.sleep(10)
        ele_username=self.find(HPL.userName)
        ActionChains(self.driver).move_to_element(ele_username).perform()
       # WebDriverWait(self.driver,10).until(self.find(HPL.simulationLogin).is_displayed())
        self.find(HPL.simulationLogin).click()
        self.find(HPL.inputUserName).send_keys(userName)
        self.find(HPL.inputUserName).send_keys(Keys.ENTER)
        self.find(HPL.selectUserName).click()
        self.find(HPL.confirmButton).click()

        time.sleep(10)



    def click_clickLanguage(self):
        ele_language=self.finds(HPL.language)[1].click()

    def click_clickProjectManagement(self):
        ele_projectManagement = self.find(HPL.projectManagement).click()
        print("33333")
        self.find(HPL.projectList).click()
