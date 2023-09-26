import time

import pytest

from Base.init_driver import init_driver_ios
from Base.get_driver import GetDriver
from Base.base import Base
from PagesUI.page_element_ios import CommonElementIos

el = CommonElementIos()

driver = GetDriver().create_driver(init_driver_ios())

base_driver = Base(driver)


# 登录
def test_login():
    base_driver.base_click(el.login)

    base_driver.base_click(el.use_email)

    base_driver.base_click(el.quick_login)


# 直播部分
def test_live():
    base_driver.base_click(el.room_page)
    time.sleep(2)
    base_driver.wait_time(el.live_tittle)
    base_driver.base_click(el.live_tittle)
    # 进入列表中第一个用户直播间
    base_driver.wait_time(el.hot_tab)
    time.sleep(2)
    base_driver.click_advance(32, 465, 68, 465)
    base_driver.wait_time(el.comment_button)
    # 操作侧滑
    base_driver.base_swipe_single(3)
    base_driver.wait_time(el.hot_live)
    base_driver.base_swipe_single(0)
    # 分享
    base_driver.base_click(el.share_live)
    base_driver.wait_time(el.share_to)
    base_driver.base_click(el.share_more)
    base_driver.wait_time(el.quit_share)
    base_driver.base_click(el.quit_share)

    # 评论
    base_driver.base_click(el.comment_button)
    base_driver.wait_time(el.send_msg)
    base_driver.base_swipe_single(0)
    base_driver.base_swipe_single(3)
    # 送礼
    time.sleep(1)
    base_driver.wait_time(el.giving_gifts)
    base_driver.base_click(el.giving_gifts)
    base_driver.click_advance(306, 768, 336, 798)
    base_driver.wait_time(el.balance_insufficient)
    base_driver.click_advance(8, 233, 12, 233)
    base_driver.base_swipe_single(0)

    # 关注
    base_driver.base_click(el.follow_img)
    # base_driver.base_click(el.follow_button)
    base_driver.base_click(el.quit_live)


def test_back():
    base_driver.base_back()


# 搜索
def test_search():
    base_driver.base_click(el.room_page)
    base_driver.base_click(el.search_button)
    base_driver.wait_time(el.input_search)
    base_driver.base_input(el.input_search, '为你写下这首情歌')
    base_driver.base_click(el.search_key)
    base_driver.wait_time(el.select_song)
    base_driver.base_click(el.select_song)


# ktv房间
def test_ktv():
    base_driver.base_click(el.room_page)
    base_driver.base_click(el.ktv_tab)
    # base_driver.base_click(el.sing_together)
    base_driver.wait_time(el.ktv_list)
    base_driver.base_click(el.ktv_list)

    # 分享
    base_driver.base_click(el.share_ktv)
    base_driver.base_click(el.share_more)
    base_driver.wait_time(el.quit_share)
    base_driver.base_click(el.quit_share)

    # 收藏
    base_driver.base_click(el.click_tittle)
    base_driver.base_click(el.click_homeowner)
    base_driver.base_click(el.follow_homeowner)

    # 送礼
    base_driver.base_click(el.send_gift)
    base_driver.base_click(el.select_gift)


# 练歌房
def test_practice_room():
    base_driver.base_click(el.room_page)
    base_driver.base_click(el.room_setting)
    base_driver.base_click(el.my_room)
    base_driver.base_click(el.select_klok)


# 退出
def test_quit():
    base_driver.base_click(el.my)
    base_driver.base_swipe_coordinate(175, 606, 175, 77, 5000)
    base_driver.wait_time(el.setting)
    base_driver.base_click(el.setting)
    base_driver.base_swipe_coordinate(175, 706, 175, 77, 5000)
    base_driver.wait_time(el.log_out)
    base_driver.base_click(el.log_out)
    base_driver.base_click(el.quit)
    driver.quit()


if __name__ == '__main__':
    pytest.main('test_ios.py')
