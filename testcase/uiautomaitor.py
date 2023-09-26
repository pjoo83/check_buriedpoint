from Base.base_uiautomator import Element
from Base.get_driver import GetDriver_u2
from Base.init_driver import init_driver_android_ui2


class test_IOS:
    def __init__(self):
        self.driver = GetDriver_u2().create_driver(init_driver_android_ui2())

    def star_app(self):
        self.driver.open_app('com.starmakerinteractive.starmaker')


test_IOS().star_app()


