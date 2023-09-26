import time
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import pytest


def test_login():
    desired_caps = {
        "platformName": "IOS",
        "appium:platformVersion": "15.6.1",
        "appium:deviceName": "iphone 8 plus",
        "appium:udid": "038354c675cac77949c24141797d17ec137091da",
        "appium:bundleId": "com.starmakerapp.starmaker",
        "appium:automationName": "XCUITest",
        "appium:noReset": False,
        "appium:webDriverAgentUrl": "http://127.0.0.1:8100",
        "appium:usePrebuiltWDA": "false",
        "appium:useXctestrunFile": "false",
        "appium:skipLogCapture": "true",
        # "appium:fullReset":True,
        # "app":r"D:\project\BuriedPoint_check\StarMaker_Develop_8.65.0_802308282259_ebb5501718.ipa"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="登录/注册"]').click()
    driver.find_element(MobileBy.XPATH, '//*[@label="使用邮箱"]').click()
    time.sleep(3)
    driver.find_element(MobileBy.XPATH, '//*[@label="keler131@sm.com"]').click()
    time.sleep(3)

    driver.find_element(MobileBy.XPATH, '//XCUIElementTypeTabBar[@name="标签页栏"]/XCUIElementTypeButton[5]').click()
    time.sleep(3)
    # el1= driver.find_element(MobileBy.XPATH,"//Table/Other[1]/Other[1]/Other[1]")

    # driver.scroll(el1,el2)
    # time.sleep(4)

    # time.sleep(3)
    # el3 = driver.find_element(MobileBy.XPATH,'//Table/Cell[1]')

    # driver.scroll(el3,el4)

    size = driver.get_window_size()
    print("设备屏幕大小：", size)

    # 4.操作APP
    # 使用swipe方法在设置首页,实现向上滑动
    # x坐标不变,y坐标从大到小
    # start_x = 0  # 不能选择屏幕的大小的边界值，否则会报错
    # start_y = 1440  # 不能选择屏幕的大小的边界值，否则会报错
    # end_x = 0
    # end_y = 400

    start_x = 175
    start_y = 606
    end_x = 175
    end_y = 77
    driver.swipe(start_x, start_y, end_x, end_y, duration=5000)

    time.sleep(3)
    el2 = driver.find_element(MobileBy.XPATH, '//*[@label="设置"]')
    el2.click()
    # el4.click()
    # driver.find_element(MobileBy.XPATH,'//*[@label="退出"]').click()

    start_x = 175
    start_y = 706
    end_x = 175
    end_y = 77
    driver.swipe(start_x, start_y, end_x, end_y, duration=5000)
    time.sleep(3)

    el4 = driver.find_element(MobileBy.XPATH, '//*[@label="登出"]')
    el4.click()

    time.sleep(1)

    el5 = driver.find_element(MobileBy.XPATH, '//*[@label="退出"]')
    el5.click()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    pytest.main('test_login1.py')
