from selenium.webdriver.common.by import By


class homePageLocator():

    logo = (By.CSS_SELECTOR,'.logo')

    language=(By.XPATH,'//div[@class="header-icon__dropdown el-dropdown"]')  #多语言
    down = (By.XPATH,"//i[@class='el-dropdown__icon el-icon-arrow-down']/..") #下拉图标

    userName = (By.XPATH,'//div[@class="header-user__name"]')  #当前登录人名称位置
    simulationLogin = (By.XPATH,'//span[(contains(text(),"模拟登录"))]')  #模拟登录按钮
    inputUserName = (By.XPATH,'//input[@class="el-input__inner" and @placeholder="请输入搜索人员"]')
    selectUserName= (By.XPATH,'//div[@title="liuww1" and text()="liuww1"]')
    confirmButton = (By.XPATH,'//button[@gppm-ui="selectUser__ok"]//span[text()="确定"]')

    projectManagement=(By.XPATH,'//span[@title="项目管理"]')
    projectList = (By.XPATH, '//span[@title="项目列表" and contains(text(),"项目列表")]')



