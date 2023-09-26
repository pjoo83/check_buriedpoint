from Base import base


class TestingCase(base):
    def __init__(self, driver):
        self.base = base(driver)
