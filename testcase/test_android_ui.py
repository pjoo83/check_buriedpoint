import time

from Base.get_driver import GetDriver_u2
from Base.init_driver import init_driver_android_ui2
from PagesUI.page_element_android import CommonElementAndroid
import pytest


@pytest.mark.usefixtures('driver_setup')
class test_IOS:
    def __init__(self):
        self.driver = GetDriver_u2().create_driver(init_driver_android_ui2())
        self.el = CommonElementAndroid()

    def test01_star_app(self):
        self.driver.open_app('com.starmakerinteractive.starmaker')

    def test_02_test_live(self):
        self.driver.click_on_element(self.el.live)
        self.driver.click_on_element(self.el.select_first_live)
        self.driver.scroll_to_ori(orientation='hr')
        time.sleep(2)
        self.driver.scroll_to_ori(orientation='hl')




test_IOS().test_02_test_live()
