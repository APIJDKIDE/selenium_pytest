import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope='session', autouse=False)
def drivers():
    global driver

    if driver is None:
        driver = webdriver.Chrome()  # GUI界面运行
        driver.maximize_window()

    return driver  # 返回驱动