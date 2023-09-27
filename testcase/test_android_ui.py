import time

from Base.get_driver import GetDriver_u2
from Base.init_driver import init_driver_android_ui2
from PagesUI.page_element_android import CommonElementAndroid
import pytest


@pytest.mark.usefixtures('driver_setup')
class test_android:
    def __init__(self):
        self.driver = GetDriver_u2().create_driver(init_driver_android_ui2())
        self.el = CommonElementAndroid()

    def test01_star_app(self):
        self.driver.open_app('com.starmakerinteractive.starmaker')

    def test02_live(self):
        """
        直播
        """
        self.driver.click_on_element(self.el.page_party)
        self.driver.click_on_element(self.el.live)
        self.driver.click_on_element(self.el.live_select)
        self.driver.phone_sleep(3)
        if self.driver.get_element(self.el.live_loading):
            self.driver.click_on_element(self.el.back_button)
            self.driver.click_on_element(self.el.live_select)
        self.driver.wait_e_dis_appear(self.el.live_anchor_follow)
        self.driver.click_on_element(self.el.live_anchor_follow)
        self.driver.scroll_to_ori(orientation='hr')
        self.driver.phone_sleep(2)
        self.driver.scroll_to_ori(orientation='hl')
        self.driver.click_on_element(self.el.live_msg)
        self.driver.wait_e_dis_appear(self.el.live_meg_text)
        self.driver.click_on_point(1032, 2050)
        # self.driver.click_on_element(self.el.live_send_msg)
        self.driver.click_on_element(self.el.back_button)

        self.driver.wait_e_dis_appear(self.el.live_share)
        self.driver.click_on_element(self.el.live_share)
        self.driver.click_on_element(self.el.back_button)
        if self.driver.wait_e_dis_appear(self.el.insufficient_balance):
            self.driver.click_on_element(self.el.back_button)
            self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.back_button)

    def test03_search(self):
        """
        搜索
        """
        self.driver.click_on_element(self.el.page_party)
        self.driver.click_on_element(self.el.search_button)
        self.driver.sent_txt_by_selector(self.el.search_text,'為你寫下這首情歌')
        self.driver.wait_e_dis_appear(self.el.search_result)
        self.driver.click_on_element(self.el.search_result)
        self.driver.wait_e_dis_appear(self.el.search_select)
        self.driver.click_on_element(self.el.search_select)
        self.driver.click_on_element(self.el.back_button)
        self.driver.click_on_element(self.el.back_button)



test_android().test03_search()
