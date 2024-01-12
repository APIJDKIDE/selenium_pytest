from selenium.webdriver.common.by import By


class loginPageLocator():

    userName = (By.ID,'username')
    passWord = (By.ID,'password')
    login = (By.CSS_SELECTOR,'.login-button')
    userAgreement = (By.XPATH,'//input[@name="private_url_a"]')  #勾选服务条款

    currentUsername = (By.XPATH, '//div[@class="header-user__name"]')  # 当前登录人名称位置
    logOut = (By.XPATH, '//span[(contains(text(),"退出"))]')  # 模拟登录按钮
    simulate = (By.XPATH, '//span[(contains(text(),"模拟登录"))]')  # 模拟登录按钮

    inputUserName = (By.XPATH,'//input[@placeholder="请输入搜索人员"]') #模拟登录弹窗上用户账号输入框
    searchButton = (By.XPATH,'//i[@class="el-input__icon el-icon-search"]') #模拟登录弹窗上的搜索按钮
    searchResults = (By.XPATH,'//tbody//tr')#模拟登录搜索结果
    selectUser = (By.XPATH,'//button[@gppm-ui="selectUser__ok"]') #模拟登录弹窗上的确定按钮