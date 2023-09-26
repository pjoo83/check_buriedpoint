import time

import pytest
from Base.driver import init_driver_android_appium
from Base.get_driver import GetDriver
from Base.base import Base
from PagesUI.page_element_android import CommonElementAndroid

driver = GetDriver().create_driver(init_driver_android_appium())
base_driver = Base(driver)
el = CommonElementAndroid()


def test_login_android():
    """
    login
    """
    base_driver.base_click(el.login)

    base_driver.base_click(el.select_email)
    base_driver.base_click(el.select_use)
    base_driver.wait_time(el.home_page)


def test_live():
    """
    直播
    """
    base_driver.base_click(el.live)
    base_driver.wait_time(el.select_first_live)
    base_driver.base_click(el.select_first_live)
    # 滑动操作
    time.sleep(4)
    base_driver.base_swipe_coordinate(800, 931, 229, 931)
    # base_driver.wait_time(el.hot_live)
    # base_driver.base_swipe_coordinate(229, 931, 800, 931)


def test_quit_android():
    """
    退出登录
    """
    base_driver.base_click(el.page_my)
    time.sleep(2)
    base_driver.wait_time(el.settings)
    base_driver.base_click(el.settings)
    time.sleep(2)
    base_driver.swipe_screen_until_to_element(el.logout)
    base_driver.wait_time(el.logout)
    base_driver.base_click(el.logout)
    base_driver.base_click(el.quit)


if __name__ == '__main__':
    pytest.main('test_android.py')
