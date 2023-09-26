from appium import webdriver

from Base.base_uiautomator import Element


class GetDriver:
    def __init__(self):
        self.driver = None

    def create_driver(self, desired_caps):
        if not self.driver:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

            return self.driver


class GetDriver_u2:
    def __init__(self):
        self.driver = None

    def create_driver(self,driver):
        if not self.driver:
            self.driver = Element(driver)

            return self.driver
